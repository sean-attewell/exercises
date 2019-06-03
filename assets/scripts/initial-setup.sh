mkdir /workspace/bitcoin
cp assets/scripts/bitcoin.conf /workspace/bitcoin/bitcoin.conf
pip3 install -r assets/scripts/requirements.txt
./assets/scripts/sync.sh
