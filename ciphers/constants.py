class Constants:
    N = 26
    A_ORD = 97
    ALPHABET = {chr(i + 97): i for i in range(N)}
    ALPHABET_NUMBERS = {i: chr(i + 97) for i in range(N)}

    CHAR_F = {
        'a': 8.2,
        'b': 1.5,
        'c': 2.8,
        'd': 4.3,
        'e': 12.7,
        'f': 2.2,
        'g': 2.0,
        'h': 6.1,
        'i': 7.0,
        'j': .2,
        'k': .8,
        'l': 4.0,
        'm': 2.4,
        'n': 6.7,
        'o': 7.5,
        'p': 1.9,
        'q': .1,
        'r': 6.0,
        's': 6.3,
        't': 9.1,
        'u': 2.8,
        'v': 1,
        'w': 2.4,
        'x': .2,
        'y': 2.0,
        'z': .1
    }

    NO_KEY_NO_LENGTH = "no key no length"
    NO_KEY_GIVEN_LENGTH = "no key given length"
    GIVEN_KEY = "given key"
