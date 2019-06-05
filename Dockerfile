FROM gitpod/workspace-full:latest
USER root
RUN yarn global add tldr

RUN sudo add-apt-repository ppa:bitcoin/bitcoin \
    && sudo apt-get update \
    && sudo apt-get install -yq bitcoind

# Copy over bashrc updates
COPY assets/scripts/bashrc.sh .
RUN cat bashrc.sh >> $HOME/.bashrc
