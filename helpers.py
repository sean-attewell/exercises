from bitcoinrpc.authproxy import AuthServiceProxy


N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
big_number = 105936749493397165751943248390023977685888340619776708311600296471039819517671

class RPC:

    def __init__(self, uri):
        self.rpc = AuthServiceProxy(uri)

    def __getattr__(self, name):
        """Hack to establish a new AuthServiceProxy every time this is called"""
        return getattr(self.rpc, name)


rpc_template = "http://%s:%s@%s:%s"
mainnet = RPC(rpc_template %
        ('bitcoin', 'python', '68.183.110.103', 8332))
testnet = RPC(rpc_template %
        ('bitcoin', 'python', 'localhost', 18332))
