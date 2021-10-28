import binascii
#create function for XOR encryption with defined key
def xorencrypt(input_s):
    k = 'blockchain'
    length_key = len(k)
    input_len = len(input_s)
    for i in range(input_len):
        k_length = i % length_key
        #loop through each character to get encryption with the given key: append each character
        input_s = (input_s[:i] +
                     chr(ord(input_s[i]) ^ ord(k[k_length])) +
                     input_s[i + 1:])



    return (input_s)


#create function to get hexadecimal representation with output of XOR encryption function
def hexadecimal(input):
    #plug in the binary output from xor encryption
    encrypted_input=xorencrypt(input)
    input_p=encrypted_input.encode(encoding='UTF-8')
    sampleString=binascii.hexlify(input_p)
    print('Hexadecimal Representation for',sentence,':', sampleString.decode(encoding='utf-8'))
    return sampleString


#run message through hexadecimal function and print output
sentence='bitcoin'
hexadecimal(sentence)

sentence='This is such a great class'
hexadecimal(sentence)