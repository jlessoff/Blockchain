import datetime
import hashlib
from bitstring import BitArray

import base64
text='Jacqueline_Lessoff:"Digital Economics"'
#create nonce ((random number, that will be changed as looped through)
nonce = 398275
found=0
#calculate starting time
d1=datetime.datetime.now()
###5 zeros
#loop through until hash meets conditions
while found==0:
    #create message as text plus nonce
    m=text+str(nonce)
    newhash1=hashlib.sha256(m.encode()).hexdigest()
    newhash = BitArray(hex=newhash1)
    newhash=(newhash.bin)
    #create conditions for hash
    if newhash[:5]=='00000':
        found=1
    #create nonce as number of loops; will loop through as hash changes
    nonce+=1
#calculate ending time
d2=datetime.datetime.now()
#print elapsed time
print('Elapsed Time: %s'%(d2-d1))
#print the binary representation
print('Binary Representation', newhash)
#print the message
print('Message', m)
#print nonce
print('Nonce',nonce)
#print hash
print('Hash:', newhash1)
#print elapsed time
#
#
# ###same process with 10 zeros
text='Jacqueline_Lessoff:"Digital Economics"'
#create nonce ((random number, that will be changed as looped through)
nonce = 238947
found=0
d1=datetime.datetime.now()
while found==0:
    m=text+str(nonce)
    newhash1=hashlib.sha256(m.encode()).hexdigest()
    newhash = BitArray(hex=newhash1)
    newhash=(newhash.bin)
    if newhash[:10]=='0000000000':
        found=1
    nonce+=1
#calculate ending time
d2=datetime.datetime.now()
#print elapsed time
print('Elapsed Time: %s'%(d2-d1))
#print the binary representation
print('Binary Representation', newhash)
#print the message
print('Message', m)
#print nonce
print('Nonce',nonce)
#print hash
print('Hash:', newhash1)
#print elapsed time

