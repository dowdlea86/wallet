# Multi-Block Chain Wallet in Python

Building a portfolio management system that supports multiple crypto-assets.  The wallet is built with the<br>
hd-wallet-derive tool.  The project also requires the python library for Bitcoin and Ethereum, "bit" and<br>
"web3.py".  The wallet can execute addresses across multiple coins but in this case we will demonstrate<br>
it's effectiveness on BTC Testnet.  We will need to write python code in the background to integrate our<br>
wallet and an outline of the code as follows:<br>

Run all the applicable imports and then create a new mnemonic code for our wallet.  We then need<br>
to set the mnemonic as an environment variable.  In python we need to use the subprocess library<br>
to derive the script.  In a command variable we need to include some important flags like our<br>
mnemomic key, coin, etc.  We then need to derive our wallet in a function.  

![derive_wallet](https://github.com/dowdlea86/wallet/blob/main/png_file/derive_wallet.png)

Once the wallet is derived, it should print 10 child accounts with respective address, index,<br>
path, privkey, pubkey, pubkeyhash, xprv, xpub.  If not formatted, it should look like as follows<br>

![accounts](https://github.com/dowdlea86/wallet/blob/main/png_file/accounts.png)

Now we will use bit and web3 for our coins and create three functions to execute our wallets.<br>
The first function we will call priv_key_to_account and will convert the child key to an account<br>
object that python library can use<br>

![priv_key_to_account](https://github.com/dowdlea86/wallet/blob/main/png_file/priv_key_to_account.png)

We then need to create a raw unsigned transaction that contains all our data and parameters needed<br>
to actually transact:<br>

![create_tx](https://github.com/dowdlea86/wallet/blob/main/png_file/create_tx.png)

We then need to create another function that will sign the transaction, and send it to the designated<br>
network.  Within the function we will call the create_tx function we created above and create a new<br>
object called raw_tx.  We will need to sign raw_tx using bit or web3.py depending on Ethereum or Bitcoin.<br>
After signing it, we will need to send the transaction to the designated blockchain network.<br>

![send_tx](https://github.com/dowdlea86/wallet/blob/main/png_file/send_tx.png)

Now we can send some transactions.  In this case we are manually setting an account that has existing <br>
BTC in it.  Otherwise you can use a testnet faucet to fund an account.  The code is simply calling<br>
the functions we created above.<br>

![transaction(https://github.com/dowdlea86/wallet/blob/main/png_file/transaction.png)

We can then check if our BTC testnet transaction was succesful by looking in a block explorer.<br>

![btctest_transaction(https://github.com/dowdlea86/wallet/blob/main/png_file/btctest_transaction.png)

The above code can also be used to send ETH and we can further write in code for other coin like
LTC.<br>



