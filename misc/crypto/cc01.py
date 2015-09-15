import binascii as ba
import base64
import codecs


# challenge 1
def hex2base64(data):
    return ba.b2a_base64(ba.unhexlify(data))[:-1].decode('utf-8')

# challenge 2
def xor(left, right):
    res = int(left, 16) ^ int(right, 16)
    hexed = '{:x}'.format(res)
    return hexed

# challenge 3
def decode_xor(encoded, key=None):
    if key is None:

        # generate possible keys
        keys = (format(int('0', 16) + i, 'x') for i in range(1, 128))

        # get keys that decode message to something alphanumeric

        decoded_msgs = []

        for k in keys:
            hex_str = decode_xor(encoded, k)
            decoded = codecs.decode(hex_str, "hex")

            try:
                decoded = decoded.decode('utf-8')
            except UnicodeDecodeError:
                pass

            if len([c for c in decoded if str(c).isalpha()]) > len(decoded)*0.6 and decoded.count(' ') > 1:
                decoded_msgs.append((ba.unhexlify(k), decoded))

        # return decoded messages
        return decoded_msgs
    else:
        encoded_key = key * int(len(encoded)/len(key))
        return xor(encoded, encoded_key).zfill(len(encoded))

def test():
    instr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    outstr = hex2base64(instr)
    assert 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == outstr

    left = '1c0111001f010100061a024b53535009181c'
    right = '686974207468652062756c6c277320657965'

    xored = '746865206b696420646f6e277420706c6179'

    assert xor(left, right) == xored

    print('tests passed')

    msg = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    msg_decoded = decode_xor(msg)
    
    for k,m in msg_decoded:
        print(k, m)

