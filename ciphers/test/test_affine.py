from ciphers.affine import Affine


def test_encrypt():
    plaintext = "secret message"
    alpha = 5
    beta = 9
    affine = Affine(plaintext, alpha, beta)
    encryption = "vdtqda rdvvjnd"
    assert(affine.encrypt() == encryption)

    plaintext = "test"
    alpha = 37
    beta = 400
    affine = Affine(plaintext, alpha, beta)
    encryption = 'lcal'
    assert(affine.encrypt() == encryption)


def test_decrypt():
    ciphertext = "vdtqda rdvvjnd"
    alpha = 5
    beta = 9
    affine = Affine(ciphertext, alpha, beta)
    decryption = 'secret message'
    assert(affine.decrypt() == decryption)

    ciphertext = "lcal"
    alpha = 37
    beta = 400
    affine = Affine(ciphertext, alpha, beta)
    decryption = 'test'
    assert(affine.decrypt() == decryption)
