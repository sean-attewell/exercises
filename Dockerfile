FROM gitpod/workspace-full:latest
USER root

# Miscellaneous package installations
RUN yarn global add tldr

# Add bitcoin aliases
RUN echo "alias bitcoind='/workspace/bitcoin/bitcoin-0.18.0/bin/bitcoind -datadir=/workspace/bitcoin/.bitcoin'" >> $HOME/.bash_aliases
RUN echo "alias bitcoin-cli='/workspace/bitcoin/bitcoin-0.18.0/bin/bitcoin-cli -datadir=/workspace/bitcoin/.bitcoin'" >> $HOME/.bash_aliases

# Update bashrc
RUN echo "export BITCOIN_DATA_DIR='/workspace/bitcoin'" >> $HOME/.bashrc \
    && echo "alias testnet='bitcoin-cli -testnet -rpcuser=bitcoin -rpcpassword=python'" >> $HOME/.bashrc \
    && echo "alias testnetd='bitcoind -testnet -prune=550'" >> $HOME/.bashrc \
    && echo "alias mainnet='bitcoin-cli -rpcuser=bitcoin -rpcpassword=python -rpcconnect=68.183.110.103'" >> $HOME/.bashrc \
    && echo "alias python='python3'" >> $HOME/.bashrc \
    && echo "alias pip='pip3'" >> $HOME/.bashrc
