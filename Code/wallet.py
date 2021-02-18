from constants import *
from web3 import Web3, Account
import subprocess
import json
import os
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

mnemonic = os.getenv('MNEMONIC', 'despair require order begin spatial glass guilt improve common where frost army venue stamp double')
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

def derive_wallets(coin=BTC, mnemonic=mnemonic):
    
    command = f'./derive -g --mnemonic={mnemonic} --coin={coin} --numderive=3 --format=jsonpretty -g'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, error) = p.communicate()
    p_status = p.wait()
    #print(json.loads(str(output)))
    #keys = json.loads(output)
    return output

test = derive_wallets(coin = BTC)
print(test)

#print(coins[COINTYPE][0]['privkey'])

coins = {'ETH':derive_wallets(coin=ETH), 'BTCTEST':derive_wallets(coin=BTCTEST)}

def priv_key_to_account(coin, privkey):
    if coin == ETH:
        return Account.privateKeyToAccount(privkey)
    elif coin == BTCTEST:
        account = PrivateKeyTestnet(privkey)
        print(account.address)
        return PrivateKeyTestnet(privkey)

        

def create_tx(coin, account, to, amount):
    if coin == ETH:
        gas_estimate = w3.eth.estimateGas(
            {'from': account.address, 'to': to, 'amount': amount}
        )
        return {
            'from': account.address,
            'to': recipient,
            'value': amount,
            'gasPrice': w3.eth.gasPrice,
            'gas': gas_estimate,
            'nonce': w3.eth.getTransactioncount(account.address),
            'chainID': w3.net.chainID
        }
    if coin == BTCTEST:
        print(account)
        print(to)
        print(amount)
        
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])




def send_tx(coin, account, to, amount):
    print(coin)
    print(account)
    print(amount)
    print(to)
    if coin == ETH:    
        raw_tx = create_tx(coin, account, to, amount)
        signed_tx = account.signTransaction(raw_tx) 
        return web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(raw_tx) 
        return NetworkAPI.broadcast_tx_testnet(signed_tx)


