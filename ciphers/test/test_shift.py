from ciphers.shift import Shift


def test_encrypt():
    plaintext = 'abc'
    key = '1'
    shift = Shift(plaintext, key)
    assert(shift.encrypt() == 'BCD')


def test_decrypt():
    ciphertext = 'bcd'
    key = '1'
    shift = Shift(ciphertext, key)
    assert(shift.decrypt() == 'ABC')


def test_decrypt_no_key():
    ciphertext = 'HAAHJRHAKHDUWSLHZL'
    key = ""
    shift = Shift(ciphertext, key)
    assert(shift.decrypt_no_key() == 'ABC')
