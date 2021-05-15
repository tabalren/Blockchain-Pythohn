# Multi-Blockchain Wallet in Python

![](coins.jpeg)

## Context

There aren't as many tools available in Python for managing multiple type of currencies in one wallet. For this activity we are using the command line tool, hd-wallet-derive that supports not only BIP32, BIP39, and BIP44, but also supports non-standard derivation paths for the most popular wallets out there today.

hd-wallet-derive is a "universal" wallet and can manage billions of addresses across 300+ coins.

We will only get 2 coins working: Ethereum and Bitcoin Testnet. Ethereum keys are the same format on any network, so the Ethereum keys should work with a custom network or testnet.

The attached code will allow you to do the following:
1. Clone and install hd-wallet-derive
2. Derive wallet keys for Bitcoin Testnet and Ether only 
3. Create and send transactions 

## HD Derive Wallet Install Guide - macOS Only

This guide serves as a step by step process for setting up the hd-wallet-derive library used to derive BIP32 addresses and private keys for Bitcoin and other alternative coins or "altcoins."

Note: The hd-wallet-derive library is written in the PHP language; therefore, you will be required to first set up PHP on your machines before installing and then running the hd-wallet-derive library.

1. Begin by opening a fresh terminal. 
2. With your terminal open, cd into your folder where you want to install your hd-wallet-derive tool and run the following code:

```  git clone https://github.com/dan-da/hd-wallet-derive
  cd hd-wallet-derive
  curl https://getcomposer.org/installer -o installer.php
  php installer.php
  php composer.phar install
```

3. You should now have a folder called hd-wallet-derive containing the PHP library!

4. To verify that you have installed it correctly, cd into your hd-wallet-derive folder and run the following command: 

``` ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change
```

5. If installation was successful, you should see output similar to what you see in the following image:

![hd-wallet-derive-execute](https://user-images.githubusercontent.com/74678703/118374321-6daaf700-b589-11eb-8c08-7639726d3ebb.png)


### Congratulations! The hd-wallet-derive library should now be working and good to go!

## Setup Project 

1. Create a project directory called wallet and cd into it.

2. Clone the hd-wallet-derive tool into this folder and install it using the [HD Wallet Derive Installation Guide](https://utoronto.bootcampcontent.com/utoronto-bootcamp/utor-tor-fin-pt-11-2020-u-c/-/blob/master/Homework/19-Blockchain-Python/Instructions/Resources/HD_Wallet_Derive_Install_Guide.md)

3. Create a symlink called derive for the hd-wallet-derive/hd-wallet-derive.php script. This will clean up the command needed to run the script in our code, as we can call ./derive instead of ./hd-wallet-derive/hd-wallet-derive.php:


Make sure you are in the top level project directory - in this case the directory named wallet.


Mac Users: Run the following command: 

``` ln -s hd-wallet-derive/hd-wallet-derive.php derive ```

4. Test that you can run the ./derive script properly, by running the following command:

``` ./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g
```

The output should match what you see below:

IMAGE here 

5. Create a file called wallet.py -- this will be your universal wallet script.


## Create and Send Transactions 

