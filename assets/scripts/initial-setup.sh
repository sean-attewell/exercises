mkdir /workspace/bitcoin
cp assets/scripts/bitcoin.conf /workspace/bitcoin/bitcoin.conf


# Install bitcoind
pushd /workspace/bin
wget -O bitcoin-0.18.0-x86_64-linux-gnu.tar.gz https://bitcoincore.org/bin/bitcoin-core-0.18.0/bitcoin-0.18.0-x86_64-linux-gnu.tar.gz
tar -xzf bitcoin-0.18.0-x86_64-linux-gnu.tar.gz && rm bitcoin-0.18.0-x86_64-linux-gnu.tar.gz
popd

pip3 install -r assets/scripts/requirements.txt
./assets/scripts/sync.sh
