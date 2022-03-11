from ciphers.shift import Shift


def test_encrypt():
    plaintext = 'abc'
    key = '1'
    shift = Shift(plaintext, key)
    assert(shift.encrypt() == 'bcd')
