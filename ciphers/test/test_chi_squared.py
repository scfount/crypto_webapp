from ciphers.chi_squared import ChiSquared
from ciphers.decryption import Decryption


def test_calculate_chi_squared():
    plaintext = "LMKSICLOVTWLTAZDMRSAFOVRSEVCIE"
    key = "x"
    decryption = Decryption(plaintext, key)
    chi = ChiSquared()
    decryption.chi_squared = chi.calculate_chi_squared(decryption)
    print(decryption.chi_squared)
    assert(decryption.chi_squared == 30.090000000000003)
