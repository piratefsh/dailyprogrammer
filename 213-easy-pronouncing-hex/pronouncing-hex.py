import re, sys

input = ['0xF5', '0xB3', '0xE4', '0xBBBB', '0xA0C9', '0xBEF0FF']

tens = {
    'A': 'atta',
    'B': 'bibbity',
    'C': 'city',
    'D': 'dickety',
    'E': 'ebbity',
    'F': 'fleventy',
    '0': '',
}
ones = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    'A': 'ehh',
    'B': 'bee',
    'C': 'cee',
    'D': 'dee',
    'E': 'eee',
    'F': 'eff'
}
for hex in input:
    parts = re.findall('([A-F0-9]{2})', re.split('0x', hex)[1])
    sys.stdout.write(hex + ' ')
    for i, part in enumerate(parts):
        if part is None: 
            continue
        pre = '' if i < 1 else 'bitey '
        padding = '' if part[1] is '0' else ' '
        sys.stdout.write(pre + tens[part[0]] + '-' + ones[part[1]] + padding)
    print()
