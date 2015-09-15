import binascii as ba
import base64
import codecs

AVG_LEN_WORD = 5

# challenge 1
def hex2base64(data):
    return ba.b2a_base64(ba.unhexlify(data))[:-1].decode('utf-8')

# challenge 2
def xor(left, right):
    res = int(left, 16) ^ int(right, 16)
    hexed = '{:02x}'.format(res)
    return hexed

# challenge 3
def decode_xor(encoded, key=None):
    # if no key given, check for all possible 128 ASCII characters
    if key is None:

        # generate possible keys
        keys = (format(int('0', 16) + i, 'x') for i in range(0, 128))

        # get keys that decode message to something alphanumeric

        decoded_msgs = []

        for k in keys:
            # get xor-ed string in hex
            hex_str = decode_xor(encoded, k)

            # decode hex into ascii
            decoded = codecs.decode(hex_str, "hex")

            # try to decode that into utf-8
            try:
                decoded = decoded.decode('utf-8')
            except UnicodeDecodeError:
                pass

            # is english if most of the characters are alphabets, and has at
            # least half of spaces expected to be in sentence based off fact
            # that average len of word is given
            if len([c for c in decoded if str(c).isalpha()]) > len(decoded)*0.6 and decoded.count(' ') > (len(decoded)/AVG_LEN_WORD)/2:
                decoded_msgs.append((ba.unhexlify(k), decoded))

        # return decoded messages
        return decoded_msgs

    # else, check for just that key
    else:
        encoded_key = key * int(len(encoded)/len(key))
        return xor(encoded, encoded_key).zfill(len(encoded))


# challenge 4
def repeating_key_xor(data, key):
    encoded = ""

    # data to hex chars
    hex_chars = string_to_hex(data)

    # generate hex of chars
    keys = list(map(char_to_hex, list(key)))

    # get xored char append encrypted byte to encoded data 
    return "".join([xor(hex_char, keys[i%len(key)]) for i,hex_char in enumerate(hex_chars)])

# helper functions
def char_to_hex(c):
    return hex(ord(c))

def string_to_hex(string):
    return [hex(ord(c))[2:] for c in string]

def get_byte_array(data):
    if len(data) % 2 == 1:
        raise ValueError("Data is not even length string")
    return [data[i:i+2] for i in range(0, len(data), 2)]

def hamming_distance(str1, str2):
    hex1 = codecs.encode(str1.encode(), 'hex_codec')
    hex2 = codecs.encode(str2.encode(), 'hex_codec')
    xored = xor(hex1, hex2).zfill(len(str1))
    bin_ver = bin(int(xored, 16))
    return bin_ver.count('1')

def test():
    # challenge 1
    instr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    outstr = hex2base64(instr)
    assert 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == outstr

    # challenge 2
    left = '1c0111001f010100061a024b53535009181c'
    right = '686974207468652062756c6c277320657965'
    xored = '746865206b696420646f6e277420706c6179'
    assert xor(left, right) == xored

    # challenge 3
    msg = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    msg_decoded = decode_xor(msg)

    for k, m in msg_decoded:
        print(k, m)

    # interlude 1
    assert get_byte_array('0100') == ['01', '00']

    # challenge 4 
    msg_in_1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    msg_out_1 = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    key = 'ICE'

    assert repeating_key_xor(msg_in_1, key) == msg_out_1
    # assert repeating_key_xor(msg_in_2, key) == msg_out_2

    # interlude 2
    assert hamming_distance('this is a test', 'wokka wokka!!!') == 37

    print('tests passed')

