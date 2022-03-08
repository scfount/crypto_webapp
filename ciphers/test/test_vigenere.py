from ciphers.vigenere import Vigenere


def test_encrypt():
    plaintext = 'attackatdawn'
    key = 'lemon'
    vigenere = Vigenere(plaintext, key)
    assert(vigenere.encrypt() == 'LXFOPVEFRNHR')


def test_decrypt():
    ciphertext = 'LXFOPVEFRNHR'
    key = 'lemon'
    vigenere = Vigenere(ciphertext, key)
    assert(vigenere.decrypt() == 'ATTACKATDAWN')
