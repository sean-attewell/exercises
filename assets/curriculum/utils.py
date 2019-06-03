import hashlib
from ecdsa import SECP256k1, SigningKey, VerifyingKey, BadSignatureError
from bitcoinrpc.authproxy import AuthServiceProxy


rpc_template = "http://%s:%s@%s:%s"
mainnet = AuthServiceProxy(rpc_template % 
        ('bitcoin', 'python', '68.183.110.103', 8332))
testnet = AuthServiceProxy(rpc_template % 
        ('bitcoin', 'python', 'localhost', 18332))


def ensure_bytes(string):
    if isinstance(string, str):
        string = string.encode()
    return string

def sha256(string):
    string = ensure_bytes(string)
    return hashlib.sha256(string).hexdigest()

def double_sha256(string):
    string = ensure_bytes(string)
    return hashlib.sha256(hashlib.sha256(string).digest()).hexdigest()


def ecdsa_sign(secret, message):
    message = ensure_bytes(message)
    sk = SigningKey.from_secret_exponent(secret, curve=SECP256k1)
    sig = sk.sign(message).hex()
    return sig

def public_key(secret):
    return SigningKey.from_secret_exponent(secret, curve=SECP256k1).get_verifying_key().to_der().hex()

def ecdsa_verify(der_pubkey_hex, signature, message):
    # cast appropriately to bytes
    message = ensure_bytes(message)
    der = bytes.fromhex(der_pubkey_hex)
    signature = bytes.fromhex(signature)

    vk = VerifyingKey.from_der(der)
    try:
        return vk.verify(signature, message)
    except BadSignatureError:
        return False

def fake_signature():
    fake_secret = randint(0, 2**256)
    return ecdsa_sign(fake_secret, "dirt")
