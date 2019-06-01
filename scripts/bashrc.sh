
# Bitcoin nodes
export BITCOIN_DATA_DIR="/workspace/.bitcoin"
export testnet="bitcoin-cli -testnet -datadir=$BITCOIN_DATA_DIR -rpcuser=bitcoin -rpcpassword=python"
export testnetd="bitcoind -testnet -datadir=$BITCOIN_DATA_DIR"
export mainnet='bitcoin-cli -rpcuser=bitcoin -rpcpassword=python -rpcconnect=68.183.110.103'
