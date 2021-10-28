from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script

def main():
    setup('testnet')
    # create transaction input from tx id of UTXO (contained 0.0042 tBTC)\n",
    trans_input = TxInput('dbe9120a331394d522625a4ebcd2833787ba7d615be59a78cd0c5a258f3653b6', 0)
    # my public key
    pub_key1 = PublicKey('027b639ba30fa0afa37e9bc0d0e72f1fbd1bbdcda7f391aa902a048ab54f0b4b51')
    pub_key1 = pub_key1.to_hex(compressed=True)
    # professor's public key
    pub_key2 = PublicKey('02019662a808d4a0df7e8c1ee8b26646e59cfaa92ebd906bde14b4bda5113fa2a9')
    pub_key2 = pub_key2.to_hex(compressed=True)
    sk = PrivateKey('cPDMeMDzz7237EQcyWx92VDHo8Pt8GTZVAL7PZU4rhkpkwPGLSC5')
    p2pk_pk = p2pk_sk.get_public_key().to_hex()
    # create the redeem script - needed to sign the transaction
    redeem_script = Script([p2pk_pk, 'OP_CHECKSIG'])

    to_addr = P2pkhAddress('n4bkvTyU1dVdzsrhWBqBw8fEMbHjJvtmJR')
    txout = TxOutput(to_satoshis(0.09), to_addr.to_script_pub_key() )
