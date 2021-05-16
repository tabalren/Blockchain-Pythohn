# Multi-Blockchain Wallet in Python

![image](https://user-images.githubusercontent.com/74678703/118403076-bf5f8a00-b63a-11eb-9d99-0c22a29a5ef5.png)


## Context

There aren't as many tools available in Python for managing multiple types of currencies in one wallet. For this activity we are using the command line tool, HD-wallet-derive that supports not only BIP32, BIP39, and BIP44, but also supports non-standard derivation paths for the most popular wallets out there today.

HD-wallet-derive is a "universal" wallet and can manage billions of addresses across 300+ coins.

We will only get 1 coin working: Bitcoin Testnet. 

The attached code will allow you to do the following:
1. Clone and install hd-wallet-derive
2. Derive wallet keys for Bitcoin Testnet and Ether only 
3. Create and send transactions 

## Dependencies

- PHP must be installed on your operating system.
- You will need to clone the [hd-wallet-derive tool](https://utoronto.bootcampcontent.com/utoronto-bootcamp/utor-tor-fin-pt-11-2020-u-c/-/blob/master/Homework/19-Blockchain-Python/Instructions/Resources/HD_Wallet_Derive_Install_Guide.md).
- [bit](https://ofek.dev/bit/) Python Bitcoin library.
- [web3.py](https://github.com/ethereum/web3.py) Python Ethereum library.


## Setup Project 

1. Create a project directory called wallet and cd into it.

2. Clone the hd-wallet-derive tool into this folder and install it using the [HD Wallet Derive Installation Guide](https://utoronto.bootcampcontent.com/utoronto-bootcamp/utor-tor-fin-pt-11-2020-u-c/-/blob/master/Homework/19-Blockchain-Python/Instructions/Resources/HD_Wallet_Derive_Install_Guide.md)

3. Create a symlink called derive for the hd-wallet-derive/hd-wallet-derive.php script. This will clean up the command needed to run the script in our code, as we can call ./derive instead of ./hd-wallet-derive/hd-wallet-derive.php:


Make sure you are in the top level project directory - in this case the directory named wallet.


Mac Users: Run the following command: 

``` ln -s hd-wallet-derive/hd-wallet-derive.php derive ```

4. Test that you can run the ./derive script properly, by running the following command:

``` ./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g ```

The output should match what you see below:

![image](https://user-images.githubusercontent.com/74678703/118402758-5592b080-b639-11eb-90bf-4ca9ee44051b.png)


5. Use the file called wallet.py -- this will be your universal wallet script and will allow you to do the following:
- Derive wallet keys for Bitcoin Testnet and Etheruem 
- Link the transaction signing libraries 
- Create a transaction using def create_tx
- Send a transaction using def send_tx

## Send Transactions 

Now, you should be able to fund this wallet using a Bitcoin testnet faucet.

1. Open up a new terminal window inside of wallet.
2. Then run the command python to open the Python shell.
3. Within the Python shell, run the command from wallet import *. This will allow you to access the functions in wallet.py interactively.
4. You'll need to set the account with  ``` priv_key_to_account ``` and use ``` send_tx``` to send transactions. See screenshot below of what you're code should look like to execute the transaction:

![image](https://user-images.githubusercontent.com/74678703/118403192-444aa380-b63b-11eb-9a6a-1ee1e6ab7f64.png)



* For a Bitcoin Testnet transaction:


1. Fund a BTCTEST address using this [testnet faucet](https://coinfaucet.eu/en/btc-testnet/?__cf_chl_jschl_tk__=666803c0e676bab635cb4d99a392c66435bf5586-1621178096-0-AZGhGOqK3fd6ijVLLzOjYNW0HDJHQdhfFhvTVbuyBTy_KGYwdLre5wpuvUPHx8jSKF8hKyutvQ2k26Td80OHARif4rmdSqZuWT698EsAjlGPjDnDrfxvyqYZAb4XNoVWD9OsqpFpFEoMvsHITc7y4euWmFho2phjji1gf0TCk3TRsiurCytKA8yVAuwkItANuGrDVZ4sxT4YbHnBeYqVSNaYV4ciUvxhhMZ9F38zBsyN7LSdguZXjZabJ1wo-9AimlmAooOJsFopBVk-zAy25HkVNLrNWbUcSJZvp9018MpREJejigVuQl-lhbWCcyRhlJ2jEPltq7DGHx05oogV2ChpgElJF1zX2fJZiGqdQzgJbxR5W7qDeL6256rvM0YUCPFSp8MyelsiGNGOARD7WWnjaD6efzlPapxsOSO4Ec1c).
2. Use a [block explorer](https://tbtc.bitaps.com/) to watch transactions on the address.
3. Send a transaction to another testnet address (either one of your own, or the faucet's).

You should be able to see the following confirmation of the transaction like so:

![image](https://user-images.githubusercontent.com/74678703/118402992-58da6c00-b63a-11eb-8b75-0a9e3ebc53bb.png)

