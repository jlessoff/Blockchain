from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey
from bitcoinutils.script import Script

def main():
    setup('testnet')
    # create transaction input from tx id of UTXO (contained 0.0042 tBTC)\n",
    trans_input = TxInput('dbe9120a331394d522625a4ebcd2833787ba7d615be59a78cd0c5a258f3653b6', 0)
    # my public key\n",
    jl_pubkey = PublicKey('027b639ba30fa0afa37e9bc0d0e72f1fbd1bbdcda7f391aa902a048ab54f0b4b51')
    jl_pubkey = jl_pubkey.to_hex(compressed=True)
    #professor's public key\n",
    lb_pubkey = PublicKey("02019662a808d4a0df7e8c1ee8b26646e59cfaa92ebd906bde14b4bda5113fa2a9")
    lb_pubkey = lb_pubkey.to_hex(compressed=True)
    # create transaction output using P2PKH scriptPubKey",
    address = P2pkhAddress('msfTfNj6FicTNBShCJBhoxvhHoM794cKsZ')
    trans_output = TxOutput(to_satoshis(0.0040), Script(['OP_DUP', 'OP_HASH160', address.to_hash160(),'OP_EQUALVERIFY', 'OP_CHECKSIG']) )
    change_address = P2pkhAddress('mpUXdqH9BALYyrp1CteptK4948Db6qe2xR')
    change_output = TxOutput(to_satoshis(0.0001), change_address.to_script_pub_key())
    # create transaction from inputs/outputs\n",
    tx = Transaction([trans_input], [trans_output, change_output])
    # print raw transaction\n",
    print("Raw unsigned transaction:" + tx.serialize())
    # my signature \n",
    priv_key = PrivateKey('')
    sig_jl = priv_key.sign_input(tx, 0, Script([2,jl_pubkey,lb_pubkey,2,'OP_CHECKMULTISIG']) )
    print("JL public sig:"+  sig_jl)
    #professor's signature(fill here)\n",
    prof_key = PrivateKey('')
    sig_lb = prof_key.sign_input(tx, 0, Script([2,jl_pubkey,lb_pubkey,2,'OP_CHECKMULTISIG']) )

    # set the scriptSig\n",
    trans_input.script_sig = Script([0,sig_jl,sig_lb])
    signed_tx = tx.serialize()
    print("\nTxId:", tx.get_txid())


if __name__ == "__main__":
    main()

