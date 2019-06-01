
# Bitcoin nodes
export BITCOIN_DATA_DIR="/workspace/exercises/.bitcoin"
export testnet-cli="bitcoin-cli -testnet -datadir=$BITCOIN_DATA_DIR -rpcuser=bitcoin -rpcpassword=python"
export testnetd="bitcoind -testnet -datadir=$BITCOIN_DATA_DIR"
export mainnet-cli='bitcoin-cli -rpcuser=bitcoin -rpcpassword=python -rpcconnect=68.183.110.103'
