# send the transaction
txid=$(testnet sendtoaddress mgGYxfX8gDySx5PQqjyZRiR12Hpe6WrPMh 0.001)
echo $txid

# inspect the transaction
testnet gettransaction $txid

# see it in out general list of transacions
testnet listtransactions

# see our balance went down (fee added on top of amount)
testnet getbalance

# check it out from the python side
# do the python exercises
# when finished
testnet listtransactions
testnet getbalance

# find address with a balance
testnet listunspent

# get private key
testnet dumpprivkey $address

# go over to python and steal these coins

# observe the theft
testnet listtransactions

# this is why you gotta protect your private keys!
