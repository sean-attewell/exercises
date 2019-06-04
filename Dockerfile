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

# Copy over bashrc updates
COPY assets/scripts/bashrc.sh .
RUN cat bashrc.sh >> $HOME/.bashrc
