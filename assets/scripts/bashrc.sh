
# Bitcoin nodes
export BITCOIN_DATA_DIR="/workspace/bitcoin"
alias testnet="bitcoin-cli -testnet -datadir=$BITCOIN_DATA_DIR -rpcuser=bitcoin -rpcpassword=python"
alias testnetd="bitcoind -testnet -datadir=$BITCOIN_DATA_DIR -prune=550"
alias mainnet='bitcoin-cli -rpcuser=bitcoin -rpcpassword=python -rpcconnect=68.183.110.103'
alias python="python3"
