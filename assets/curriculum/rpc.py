from utils import testnet
from pprint import pprint

print(testnet.getblockchaininfo())  # etc
print(pprint(testnet.getblockchaininfo()))  # etc

# btw there's also a mainnet 
# TODO: maybe define genesis_hash in utils.py?
from utils import mainnet

print(mainnet.getblock("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"))

# btw there is a `mainnet` in the terminal, too
