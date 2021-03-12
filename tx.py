import bit


def load():
    f = open('secrets.txt', 'r')
    contents = f.read()
    return bit.PrivateKeyTestnet.from_hex(contents) 

# def send():
#     key = load() # private key from contents now as bit object. Doing key.address gives associated address miecNwDucUjGkjedPpCaz8puqusqdobizL
#     address = 'mphj8FzXg9dDTYBPKf3urpci8QWNLkRqPw' # generated on command line with testnet getnewaddress '' 'legacy'
#     outputs = [
#         (address, '0.001', 'btc')
#     ]
#     key.send(outputs)

#     print(key.get_transactions())
#     print(key.get_balance())

def send(key, address, amount):
    outputs = [
        (address, amount, 'btc')
    ]
    key.send(outputs)


def steal():
    # this is the private key you got by testnet listunspent, then testnet dumpprivkey 2NERK4JsGpDqPsri2csRZCXthfDqrBWhELr (an address you found in unspent)
    wif = 'cNmtVUSXKaiVd673YL9K8sA9ERtgEwb5UyhhcSg5dHeu1t2Lgzoq' # a private key serialized to the Wallet Import Format. 
    their_key = bit.PrivateKeyTestnet(wif) # turn it into a private key testnet instance
    our_key = load() # load our key to generate our address
    send(their_key, our_key.address, 0.0123) # send it to ourselves


steal()