from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import binascii

#load LB public key from file and convert to bytes
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
    )
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    pem.splitlines()[0]
    #encrypt message of my choosing and print ciphertext
    message=b"I just invested all of my savings in bitcoin"
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Question 2.1: send a message encrypted with public key:",ciphertext)

#converting message to hexidecimal form, and encrypting  with LB public key for question 4
    message2=binascii.hexlify(b"Am I doing this correctly?")
    ciphertext2 = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )



#generate keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

#print public key
public = private_key.public_key()
public_key_JL = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("Question 2.2: Generate an RSA key pair.  Send me the Public Key",public_key_JL)

#signing a message with my private key

signature = private_key.sign(
    ciphertext2,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)


#print output
print("Question 2.3: Send me the message and signature.")
print('Message:',message2.decode('utf-8'))
print("New message encrypted with your public key:",ciphertext2)
print("Signature:",signature)
