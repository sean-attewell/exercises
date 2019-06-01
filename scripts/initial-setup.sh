mkdir /workspace/bitcoin
cp scripts/bitcoin.conf /workspace/bitcoin/bitcoin.conf
pip3 install -r scripts/requirements.txt
./scripts/sync.sh
