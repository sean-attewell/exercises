from bit import PrivateKeyTestnet, verify_sig

# in repl
private_key = PrivateKeyTestnet()
print(private_key.to_hex())
print(private_key.to_der())
print(private_key.to_pem())
print(private_key.to_wif())
print(private_key.to_bytes())
# but it's really just an integer under the hood
print(private_key.to_int())
print(PrivateKeyTestnet.from_int(int(private_key.to_hex(), 16)))

# less than N
from helpers import N
print(private_key.to_int() < N)

# we can sign messages
msg = 'hello, world, hello'.encode()
sig = private_key.sign(msg)
print('signature')
print(sig)
print(sig.hex())  # have them do this second

# we can verify signatures
print('verifies?')
print(private_key.verify(sig, msg))

# FIXME: can't figure out how to verify the signature using bitcoin-cli
# I think it has to do w/ base64 encoding, which bitcoin-cli expects
# bitcoin-cli's signatures are 88 bytes, when i base64 encode sig above
# i get 96 bytes. some extra shit is sneaking in ...

# also derives a bitcoin address. this is more ergonomic than ^^
# we saw this earlier
# let's fund this
print('address')
print(private_key.address)

