from bitcoinutils.setup import setup
from bitcoinutils.utils import to_satoshis
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.keys import P2pkhAddress, PrivateKey
from bitcoinutils.script import Script
from bitcoinutils.constants import SIGHASH_ALL, SIGHASH_NONE, SIGHASH_SINGLE, SIGHASH_ANYONECANPAY


def main():
    setup('testnet')

#create a transaction input from tx id
    # 0.001 tBTC
    txin1 = TxInput('560063f27acb65a4106b420c6a8e98e19dcbdfd4d700228dcc7ebeceda635aa9', 1)
    # 0.0001 tBTC
    txin2 = TxInput('9b2cb2fb72d53a10a3d95cf6c963dba5b9d349c980145e2f0d870d6fd6495fcb', 0)
    #0.00095756 tbc
    txin3 = TxInput("26ae40eb2231ab07fd0175775d6474bd2b289e33d0fabcadc45b87846a713e20", 0)
    #0.0008
    txin4 = TxInput("0f67120268b567370ef24ba3ce1d2e88681aac38c67eb97f9eeb470fe71a133e", 0)
    #0.0008
    txin5 = TxInput("5887b151a91684b6819e8692360087fcda64b2a9eccb99e2d169b6145f815e97", 1)
    #0.00005
    txin6 = TxInput("cb5a5970e789e97e59cf08019b1ccb73b05371778cdd2e1218896bda502fc9ae", 1)
    #0.00062612
    txin7 = TxInput("fdb815e482bf96a3fb86565fe2ba6dd9eefec9c584bbe5e8074ad4a5e8bf8be7", 0)
    #0.0009 -> 0.0.00578368
    txin8 = TxInput("458e4a6afb36fe0e7dfe30fc105efdd294b96ca54e44a6ff6b36ad2357b49e46", 1)


# create transaction output using P2PKH scriptPubKey (locking script)
    addr = P2pkhAddress('mreLpAzPWBtdwBC9NMEsBy1jkQ3phjy1Eh')
    txout = TxOutput(to_satoshis(0.0055),  Script(['OP_DUP', 'OP_HASH160', addr.to_hash160(),'OP_EQUALVERIFY', 'OP_CHECKSIG']) )
    change_addr = P2pkhAddress('mpUXdqH9BALYyrp1CteptK4948Db6qe2xR')
    change_txout = TxOutput(to_satoshis(0.00018368),change_addr.to_script_pub_key())

    tx = Transaction([txin1,txin2,txin3,txin4,txin5,txin6,txin7,txin8], [txout, change_txout])
    print("\nRaw unsigned transaction:\n" + tx.serialize())
    sk = PrivateKey('')
    from_addr = P2pkhAddress('mpUXdqH9BALYyrp1CteptK4948Db6qe2xR')

    sig1 = sk.sign_input(tx, 0, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    sig2 = sk.sign_input(tx, 1, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    sig3 = sk.sign_input(tx, 2, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    sig4 = sk.sign_input(tx, 3, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    sig5 = sk.sign_input(tx, 4, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    sig6 = sk.sign_input(tx, 5, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    sig7 = sk.sign_input(tx, 6, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))
    sig8 = sk.sign_input(tx, 7, Script(
        ['OP_DUP', 'OP_HASH160', from_addr.to_hash160(), 'OP_EQUALVERIFY', 'OP_CHECKSIG']))



    pk = sk.get_public_key().to_hex()
    print(pk)
    txin1.script_sig=Script([sig1,pk])

    txin2.script_sig=Script([sig2,pk])

    txin3.script_sig=Script([sig3,pk])

    txin4.script_sig=Script([sig4,pk])

    txin5.script_sig=Script([sig5,pk])

    txin6.script_sig=Script([sig6,pk])

    txin7.script_sig=Script([sig7,pk])
    txin8.script_sig=Script([sig8,pk])

    signed_tx = tx.serialize()
    print("\nRaw signed transaction:\n" + (signed_tx))
    print("\nTxId:", tx.get_txid())

if __name__ == "__main__":
    main()
