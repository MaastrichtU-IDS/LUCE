#!/bin/sh

# conda init bash
# conda activate luce_vm

# Start Django on port 8000
nohup python /luce/luce_django/luce/manage.py runserver 0.0.0.0:8000 --noreload &


# Start Ganache on port 8545
# nohup ganache-cli --mnemonic luce --db ~/.ganache_db --networkId 72 --host 0.0.0.0 --accounts 1000 --defaultBalanceEther 1000000 &
nohup ganache-cli --mnemonic luce --db ~/.ganache_db --networkId 72 --host 0.0.0.0 --accounts 3 --defaultBalanceEther 1000000 &


# Send in commands to start Ethereum private testnet on port 8544
#nohup geth --identity node1 --networkid 4224 --mine --miner.threads 1 --datadir "/luce/ethtestnet/node1" --nodiscover --rpc --rpcport "8544" --port "30302" --rpccorsdomain "*" --nat "any" --rpcapi admin,miner,eth,web3,personal,net --allow-insecure-unlock --password /luce/ethtestnet/node1/password.sec --ipcpath "~/.ethereum/geth.ipc" &

echo "Visit http://127.0.0.1:8888 to access the Jupyter notebook environment. The password is: luce"
echo "Visit http://127.0.0.1:8000 to access the Luce Data Exchange."
echo "Demo accounts:"
echo "provider@luce.com   | provider"
echo "requester@luce.com  | requester"

# Start JupyterLab server on port 8888
exec jupyter lab --allow-root --no-browser --ip 0.0.0.0 --notebook-dir=/luce/jupyter/
