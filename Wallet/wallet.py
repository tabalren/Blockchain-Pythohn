# Import dependencies
import os
import subprocess
import json
from dotenv import load_dotenv
from pprint import pprint

# Load and set environment variables
load_dotenv()
mnemonic= "loop ring practice orbit balcony island lecture victory cat hurry chicken story"

# Import constants.py and necessary functions from bit and web3
from constants import *
from bit import Key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI 
from eth_account import Account 
from web3 import Web3
from web3.auto.gethdev import w3
from web3.middleware import geth_poa_middleware

# Create a function called `derive_wallets`
def derive_wallets(coin): 
    command = f'./derive -g --mnemonic="{mnemonic}"--cols=path,address,privkey,pubkey --format=json --coin="{coin}" --numderive=3' 

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    return keys

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
   ETH: derive_wallets(ETH), # 'eth':{[], [], []}
   BTCTEST: derive_wallets(BTCTEST)
  }
pprint(coins)


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.

def priv_key_to_account(coin, priv_key):
    if coin == BTCTEST:
        return bit.PrivateKeyTestnet(priv_key) 
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)


eth_acc = priv_key_to_account(ETH,'0x8faec32ac1548d4afd80e922c3413d3dcfcb9642338cb6b54e9750c5d73fa652') 
btc_acc = priv_key_to_account(BTCTEST,'cPYBHKDbhYaXpcMKBqVSWQegH7t2VMnP3S6XntVAZdSisqW1WMEF') 

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin,account,to,amount):
    if coin == BTCTEST:
        return bit.PrivateKeyTestnet.prepare_transaction(account.address, [(to,amount,BTC)])
    elif coin == ETH:
        value=w3.toWei(amount, 'ether')
        gas_estimate = w3.eth.estimateGas(
            {'from': account.address,'to': to, 'amount': value}
            )
        return {
            'from': account.address,
            'to': to,
            'value': value,
            'gasPrice': w3.eth.generateGasPrice(),
            'gas': gas_estimate,
            'nonce':w3.eth.get.getTransactionCount(account.address), 
            'chainId': w3.eth.chain_id()
        }

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
#def send_tx(# YOUR CODE HERE):
def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    if coin==ETH: 
        signed_tx = account.signTransaction(tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    elif coin == BTCTEST: 
        signed_tx=account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx)
