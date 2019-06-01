FROM gitpod/workspace-full:latest
USER root
RUN yarn global add tldr

#USER gitpod
#ENV PATH=$HOME/.pyenv/bin:$HOME/.pyenv/shims:$PATH
#RUN pyenv global 2.7.15 3.7.2 \
    #&& sudo pip3 install -r requirements.txt
RUN sudo add-apt-repository ppa:bitcoin/bitcoin \
    && sudo apt-get update \
    && sudo apt-get install -yq bitcoind



#RUN echo "alias testnet-cli='bitcoin-cli -testnet -datadir=/workspace/exercises/.bitcoin'" >> $HOME/.bashrc
#RUN echo "alias mainnet-cli='bitcoin-cli -rpcuser=bitcoin -rpcpassword=python -rpcconnect=68.183.110.103'" >> $HOME/.bashrc
#RUN echo "alias testnetd='bitcoind -testnet -datadir=/workspace/exercises/.bitcoin'" >> $HOME/.bashrc
RUN cat /workspace/exercises/bashrc >> $HOME/.bashrc


#USER root
