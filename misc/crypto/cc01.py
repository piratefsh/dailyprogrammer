import binascii as ba
import base64
import codecs

AVG_LEN_WORD = 5


def hex2base64(data):
    """
    challenge 1. returns string in hex encoded into base64
    """
    return ba.b2a_base64(ba.unhexlify(data))[:-1]


def base642hex(data):
    padded = pad64(data)
    try:
        decoded64 = base64.b64decode(pad64(data))
    except ba.Error:
        return None
    return ba.hexlify(decoded64)


def pad64(bytestring):
    missing = 4 - len(bytestring) % 4
    return bytestring + b'=' * missing if missing > 0 else bytestring


def xor(left, right):
    """
    challenge 2. xors two strings of equal length and returns string
    """
    res = int(left, 16) ^ int(right, 16)
    hexed = '{:02x}'.format(res)  # int to string format
    return hexed


def decode_xor(encoded):
    """
    challenge 3: decodes an xor-ed message with all possible single character key
    """
    # generate possible keys ['1', '2', ... 'e', 'f']
    keys = (format(i, 'x') for i in range(128))

    decoded_msgs = []

    for k in keys:
        # get xor-ed string in hex
        hex_str = decode_xor_one(encoded, key=k)

        # decode hex into ascii
        decoded = codecs.decode(hex_str, "hex")

        # try to decode that into utf-8
        try:
            decoded = decoded.decode('utf-8')
        except UnicodeDecodeError:
            pass

        if is_english_kinda(decoded):
            decoded_msgs.append((ba.unhexlify(k), decoded))

    # return decoded messages
    return decoded_msgs


def decode_xor_one(encoded, key):
    """
    challenge 3 helper. decodes message with a given single character key
    """

    encoded_key = key * int(len(encoded)/len(key))
    return xor(encoded, encoded_key).zfill(len(encoded))


def is_english_kinda(decoded):
    """ 
    challenge 3 helper. 
    is english if most of the characters are alphabets, and has at
    least half of spaces expected to be in sentence based off fact
    that average len of word is given 
    """
    num_alpha = len([c for c in decoded if str(c).isalpha()])
    num_expected_spaces = (len(decoded)/AVG_LEN_WORD)

    decent_alpha_ratio = num_alpha > len(decoded)*0.6
    decent_num_spaces = decoded.count(' ') > num_expected_spaces/2
    return decent_alpha_ratio and decent_num_spaces


def repeating_key_xor(data, key):
    """
    challenge 4: decodes xor-ed message with a repeating key
    """

    encoded = ""

    # data to hex chars
    hex_chars = string_to_hex(data)

    # generate hex of chars
    keys = list(map(char_to_hex, list(key)))

    # get xored char append encrypted byte to encoded data
    return "".join([xor(hex_char, keys[i % len(key)])
                    for i, hex_char in enumerate(hex_chars)])


def decode_repeating_key_xor(filename):
    # find keysize
    f = open(filename, 'rb')
    keysize, distance = get_min_hamming_dist_keysizes(f, 1)[0]

    # break text into keysize blocks
    blocks = get_file_blocks(f, keysize)

    # transpose blocks
    transposed = get_transposed_blocks(blocks, keysize)

    # solve each block as single char xor
    return


def get_transposed_blocks(blocks, keysize):
    return [[block[byte] for block in blocks] for byte in range(keysize)]


def get_file_blocks(f, size):
    f.seek(0)
    blocks = []
    while True:
        block = f.read(size)
        if block:
            blocks.append(block)
        else:
            break
    return blocks


def get_min_hamming_dist_keysizes(f, n):
    keysizes = range(2, 40)
    normalized_hammings = []
    for keysize in keysizes:
        f.seek(0)
        left = base642hex(f.read(keysize))
        right = base642hex(f.read(keysize))

        if(left is None or right is None):
            continue

        hd = hamming_distance_bytes(left, right)/keysize
        normalized_hammings.append((keysize, hd))
    normalized_hammings.sort(key=lambda x: x[1])
    return normalized_hammings[0:n]

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
    hex1 = ba.hexlify(str1.encode())
    hex2 = ba.hexlify(str2.encode())
    return hamming_distance_bytes(hex1, hex2)


def hamming_distance_bytes(bytechunk1, bytechunk2):
    xored = xor(bytechunk1, bytechunk2)
    bin_ver = bin(int(xored, 16))
    return bin_ver.count('1')


def test():
    # challenge 1
    instr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    outstr = hex2base64(instr).decode('utf-8')
    assert 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == outstr

    # challenge 2
    left = '1c0111001f010100061a024b53535009181c'
    right = '686974207468652062756c6c277320657965'
    xored = '746865206b696420646f6e277420706c6179'
    assert xor(left, right) == xored

    # challenge 3
    msg = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    msg_decoded = decode_xor(msg)

    assert msg_decoded[0][1] == "Cooking MC's like a pound of bacon"

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

    filename = 'cc06in.txt'
    f = open(filename, 'rb')
    keysize, dist = get_min_hamming_dist_keysizes(f, 1)[0]
    assert keysize == 4

    # check all blocks are of len keysize
    blocks = get_file_blocks(f, keysize)
    assert len([b for b in blocks if len(b) != keysize]) == 0

    # check transposed blocks
    assert len(get_transposed_blocks(blocks, keysize)) == keysize

    print('tests passed')
