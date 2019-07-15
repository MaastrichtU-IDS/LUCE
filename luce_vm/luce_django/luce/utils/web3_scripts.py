from web3 import Web3
import time
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

def create_wallet():
	print("This message comes from within my custom script")
	
	class EthAccount():
	    address = None
	    pkey = None

	def create_wallet():
	    eth_account = EthAccount()
	    eth_account_raw = w3.eth.account.create()
	    eth_account.address = eth_account_raw.address
	    eth_account.pkey = eth_account_raw.privateKey
	    return (eth_account)

	eth_account = create_wallet()

	# Extract default accounts created by ganache
	accounts = w3.eth.accounts

	# Instantiate faucet object
	faucet = EthAccount()

	# Wallet address
	faucet.address       = "0x92D44e8579620F2Db88A12E70FE38e8CDB3541BA"
	# Private key (from Ganache interface)
	faucet.pkey   = "0x4a2cb86c7d3663abebf7ab86a6ddc3900aee399750f35e65a44ecf843ec39116"

	# Define a function to send ether

	def send_ether(amount_in_ether, recipient_address, sender_address = faucet.address, sender_pkey=faucet.pkey):
	    amount_in_wei = w3.toWei(amount_in_ether,'ether');

	    # How many transactions have been made by wallet?
	    # This is required and prevents double-spending.
	    # Different from nonce in block mining.
	    nonce = w3.eth.getTransactionCount(sender_address)
	    
	    # Specify transcation dictionary
	    txn_dict = {
	            'to': recipient_address,
	            'value': amount_in_wei,
	            'gas': 2000000,
	            'gasPrice': w3.toWei('40', 'gwei'),
	            'nonce': nonce,
	            'chainId': 3
	    }
	    
	    # Sign transaction
	    signed_txn = w3.eth.account.signTransaction(txn_dict, sender_pkey)

	    # Send transaction & store transaction hash
	    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

	    # Check if transaction was added to blockchain
	    # time.sleep(0.5)
	    txn_receipt = w3.eth.getTransactionReceipt(txn_hash)
	    return txn_hash

	# Send ether and store transaction hash
	txn_hash = send_ether(1.5,eth_account.address)

	# Show balance
	print("The balance of the new account is:\n")
	print(w3.eth.getBalance(eth_account.address))

	import os
 
	dirpath = os.getcwd()
	print("current directory is : " + dirpath)
	foldername = os.path.basename(dirpath)
	print("Directory name is : " + foldername)


def assign_address(user):
    # Establish web3 connection
    from web3 import Web3
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    accounts = w3.eth.accounts
    # Obtain user model
    from django.contrib.auth import get_user_model
    User = get_user_model()
    # Obtain user count
    user_count = len(User.objects.all())
    idx = user_count-1
    # Assign web3 account to user
    current_user = user
    current_user.ethereum_public_key = accounts[idx]
    current_user.save()
    # Return user with address associated
    return current_user



def deploy_contract(user):
    from solcx import compile_source
    from web3 import Web3
    
    # Read in LUCE contract code
    with open('./utils/data/luce.sol', 'r') as file:
        contract_source_code = file.read()
        
    # Compile & Store Compiled source code
    compiled_sol = compile_source(contract_source_code)

    # Extract full interface as dict from compiled contract
    contract_interface = compiled_sol['<stdin>:Dataset']

    # Extract abi and bytecode
    abi = contract_interface['abi']
    bytecode = contract_interface['bin']
    
    # Establish web3 connection
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

    # Obtin user
    current_user = user
    
    # Set sender
    w3.eth.defaultAccount = current_user.ethereum_public_key

    # Create contract blueprint
    Luce = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Submit the transaction that deploys the contract
    tx_hash = Luce.constructor().transact()
    
    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    # Obtain address of freshly deployed contract
    contractAddress = tx_receipt.contractAddress

    return contractAddress


def deploy_contract_with_data(user, description, license, link=""):
    from solcx import compile_source
    from web3 import Web3
    
    # Read in LUCE contract code
    with open('./utils/data/luce.sol', 'r') as file:
        contract_source_code = file.read()
        
    # Compile & Store Compiled source code
    compiled_sol = compile_source(contract_source_code)

    # Extract full interface as dict from compiled contract
    contract_interface = compiled_sol['<stdin>:Dataset']

    # Extract abi and bytecode
    abi = contract_interface['abi']
    bytecode = contract_interface['bin']
    
    # Establish web3 connection
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

    # Obtin user
    current_user = user
    
    # Set sender
    w3.eth.defaultAccount = current_user.ethereum_public_key

    # Create contract blueprint
    Luce = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Submit the transaction that deploys the contract
    tx_hash = Luce.constructor().transact()
    
    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    # Obtain address of freshly deployed contract
    contract_address = tx_receipt.contractAddress
    
    # Create python instance of deployed contract
    luce = w3.eth.contract(
    address=contract_address,
    abi=contract_interface['abi'],
    )
    
    # Store dataset information in contract
    tx_hash = luce.functions.publishData(description, link, license).transact()
    
    return contract_address
	


def fund_wallet():
	pass