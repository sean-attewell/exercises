import bit

def generate():
    key = bit.PrivateKeyTestnet()
    f = open('secret.txt', 'w')
    f.write(key.to_hex())
    print('wrote secret to secret.txt')
    f.close()
    return key

def load():
    f = open('secret.txt')
    key_hex = f.read()
    return bit.PrivateKeyTestnet.from_hex(key_hex)
    




### after we send coins here from bitcoin-cli

# balance
def get_state():
    key.get_balance()
    key.get_transactions()
    key.get_unspent()

# do it by hand first, then make a function (re-used by steal)
def send(key, address):
    tx = key.create_transaction(
        [(address, .0002, 'btc')],
        2
    )
    print(bit.network.NetworkAPI.broadcast_tx_testnet(tx))
    print('tx id is: ', key.get_transactions()[0])
    # go check bitcoin-cli

# send(load(), "2N5cXk4t6ryeXcCRj8YHbuv9sQkyZ7h8wJy")

def steal(wif_key):
    my_key = load()
    their_key = bit.wif_to_key(wif_key)
    send(their_key, my_key.address)

# steal('cNz3TZUuKsFMo6hAyNS8s4DG7kPPpQ7MzTmeckPgJF7uheL7HssN')

# go over to bitcoin-cli to observe the theft!
