#-------------------------------------------------------------------------------
# Challenge 246I: Letter splits.
#           Date: December 23, 2015
#-------------------------------------------------------------------------------
import time


def num_to_char(num):
    return chr(ord('A') - 1 + num)


def decode(encoded):
    if len(encoded) == 0:
        return ['']  # Valid (just an empty string).

    first = int(encoded[0])
    if first == 0:
        return []  # Invalid (no candidates).

    if len(encoded) == 1:
        return [num_to_char(int(encoded))]

    candidates = []

    prefix = num_to_char(first)
    candidates.extend(prefix + suffix for suffix in decode(encoded[1:]))

    first_two = int(encoded[:2])
    if 1 <= first_two <= 26:
        prefix = num_to_char(first_two)
        candidates.extend(prefix + suffix for suffix in decode(encoded[2:]))

    return candidates


def main():
    encoded = '1234567899876543210'
    candidates = decode(encoded)
    for candidate in candidates:
        print(candidate)


def split(word):
    return [(word[:i+1], word[i+1:]) for i in range(len(word))]


def segment(word, vocab):
    if not word:
        return [[]]

    candidates = []
    splits = split(word)
    for first, rest in splits:
        if first in vocab:
            for suffix in segment(rest, vocab):
                candidate = [first] + suffix
                candidates.append(candidate)

    return candidates


def bonus():
    start = time.time()
    with open('enable1.txt') as f:
        vocab = set(f.read().split())

    encoded = '81161625815129412519419122516181571811313518'

    best_guess = ''
    min_length = float('inf')
    num_guesses = 0
    candidates = decode(encoded)
    print(len(candidates))
    for candidate in candidates:
        sentences = segment(candidate.lower(), vocab)
        for sentence in sentences:
            num_guesses += 1
            guess = ' '.join(sentence).upper()
            if len(guess) < min_length:
                best_guess = guess
                min_length = len(best_guess)

    print('     Elapsed Time: %f seconds.' % (time.time() - start))
    print('Number of Guesses: %d.' % num_guesses)
    print('       Best Guess: %s' % best_guess)


bonus()