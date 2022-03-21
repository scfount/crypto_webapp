from ciphers.affine import Affine


def test_encrypt():
    plaintext = "secret message"
    alpha = 5
    beta = 9
    affine = Affine(plaintext, alpha, beta)
    encryption = "vdtqdardvvjnd"
    assert(affine.encrypt() == encryption.upper())

    plaintext = "test"
    alpha = 37
    beta = 400
    affine = Affine(plaintext, alpha, beta)
    encryption = 'lcal'
    assert(affine.encrypt() == encryption.upper())


def test_decrypt():
    ciphertext = "vdtqdardvvjnd"
    alpha = 5
    beta = 9
    affine = Affine(ciphertext, alpha, beta)
    decryption = 'SECRETMESSAGE'
    assert(affine.decrypt() == decryption)

    ciphertext = "lcal"
    alpha = 37
    beta = 400
    affine = Affine(ciphertext, alpha, beta)
    decryption = 'TEST'
    assert(affine.decrypt() == decryption)
