from ciphers.shift import Shift


def test_encrypt():
    plaintext = 'abc'
    key = '1'
    shift = Shift(plaintext, key)
    assert(shift.encrypt() == 'bcd')


def test_decrypt():
    ciphertext = 'bcd'
    key = '1'
    shift = Shift(ciphertext, key)
    decryptions = shift.decrypt()
    assert(decryptions[0].text == 'abc')


def test_decrypt_no_key():
    ciphertext = 'HAAHJRHAKHDUWSLHZL'
    key = ""
    shift = Shift(ciphertext, key)
    decryptions = shift.decrypt_no_key()
    assert(decryptions[0].text == 'attackatdawnplease')
