FROM gitpod/workspace-full:latest
USER root
RUN yarn global add tldr
RUN sudo python3 -m pip install -r requirements.txt
RUN sudo add-apt-repository ppa:bitcoin/bitcoin \
    && sudo apt-get update \
    && sudo apt-get install bitcoind \
    && python3 -m pip install -r requirements.txt
