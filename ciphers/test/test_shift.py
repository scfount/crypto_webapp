from shift import Shift


def test_encrypt():
    plaintext = 'abc'
    key = '1'
    assert(Shift.encrypt(plaintext, key) == 'bcd')
