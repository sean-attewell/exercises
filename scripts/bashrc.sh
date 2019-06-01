
# Bitcoin nodes
BITCOIN_DATA_DIR="/workspace/.bitcoin"
alias testnet-cli="bitcoin-cli -testnet -datadir=$BITCOIN_DATA_DIR -rpcuser=bitcoin -rpcpassword=python"
alias testnetd="bitcoind -testnet -datadir=$BITCOIN_DATA_DIR"
alias mainnet-cli='bitcoin-cli -rpcuser=bitcoin -rpcpassword=python -rpcconnect=68.183.110.103'
