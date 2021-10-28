from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script


def main():
    setup('testnet')
    #my public key
    pub_key1 = PublicKey('027b639ba30fa0afa37e9bc0d0e72f1fbd1bbdcda7f391aa902a048ab54f0b4b51')
    pub_key1 = pub_key1.to_hex(compressed=True)
    #professor's public key
    pub_key2 = PublicKey('02019662a808d4a0df7e8c1ee8b26646e59cfaa92ebd906bde14b4bda5113fa2a9')
    pub_key2 = pub_key2.to_hex(compressed=True)
    # create transaction input
    #0.001
    tx1 = TxInput('7f7e7d4a7453f826fa8254f94148de27a58b6b75f19c4fec205c11f6ac6bd63f', 0)
    #0.00088374
    tx2 = TxInput('1a8fd25bd60a93ca9c16d301a9d64e61b3d5b41a0c1508f13ab1c2601df04a2a', 1)
    #0.0008
    tx3 = TxInput('a0aed1f1abea93c1e35db9b5e2bff168fc4828a1ba6e542095d66b26a19ee78e', 1)
    #0.0008 tBTC 0.00348374
    tx4 = TxInput('4688b4a1e8353d75f305b28a85ba18b7f229a650658f262f6bf0eea40f03e8a1', 1)
    #.00446936
    tx5 = TxInput('d11da2f399635709c501ecf532ab1ba7afa9f7ee5a579378a318aef65d990769', 1)

    # create transaction output using P2PKH scriptPubKey\n",
    trans_output = TxOutput(to_satoshis(0.0042), Script([2,pub_key1,pub_key2,2,'OP_CHECKMULTISIG']) )
    change_address = P2pkhAddress('mpUXdqH9BALYyrp1CteptK4948Db6qe2xR')
    change_output = TxOutput(to_satoshis(0.0002),  Script(['OP_DUP', 'OP_HASH160',change_address.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))

    # create transaction from inputs/outputs\n",
    tx = Transaction([tx1,tx2,tx3,tx4,tx5], [trans_output, change_output])
    # print raw transaction\n",
    print("Raw unsigned transaction:" + tx.serialize())
 #create signature\n",
    sk = PrivateKey('cPDMeMDzz7237EQcyWx92VDHo8Pt8GTZVAL7PZU4rhkpkwPGLSC5')
    from_address = P2pkhAddress('mpUXdqH9BALYyrp1CteptK4948Db6qe2xR')
    sig1 = sk.sign_input(tx, 0, Script(['OP_DUP', 'OP_HASH160',from_address.to_hash160(), 'OP_EQUALVERIFY','OP_CHECKSIG']) )
    sig2 = sk.sign_input(tx, 1, Script(['OP_DUP', 'OP_HASH160',from_address.to_hash160(), 'OP_EQUALVERIFY','OP_CHECKSIG']) )
    sig3 = sk.sign_input(tx, 2, Script(['OP_DUP', 'OP_HASH160',from_address.to_hash160(), 'OP_EQUALVERIFY','OP_CHECKSIG']) )
    sig4 = sk.sign_input(tx, 3, Script(['OP_DUP', 'OP_HASH160',from_address.to_hash160(), 'OP_EQUALVERIFY','OP_CHECKSIG']) )
    sig5 = sk.sign_input(tx, 4, Script(['OP_DUP', 'OP_HASH160',from_address.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']) )
    # get public key as hex\n",
    pub_key = sk.get_public_key().to_hex()
    print("\nTxId:", tx.get_txid())

    # set the scriptSig \n",
    tx1.script_sig = Script([sig1, pub_key])
    tx2.script_sig = Script([sig2, pub_key])
    tx3.script_sig = Script([sig3, pub_key])
    tx4.script_sig = Script([sig4, pub_key])
    tx5.script_sig = Script([sig5, pub_key])
    signed_tx = tx.serialize()
  # print raw signed transaction ready to be broadcasted\n",
    print("Raw signed transaction:" + signed_tx)

if __name__ == "__main__":
    main()
