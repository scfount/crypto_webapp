from operator import inv
import string

from pyparsing import alphanums
from .constants import Constants


class Affine:

    def __init__(self, text, alpha, beta) -> None:
        self.text = text.lower()
        self.alpha = int(alpha)
        self.beta = int(beta)

    def encrypt(self):
        '''
        Function --
            Affine Cipher encryption of plaintext
            y = ax + b % 26
        Parameters --
        Returns --
            String, ciphertext
        '''

        plaintext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []
        for char in plaintext:
            encrypt_char = (
                (Constants.ALPHABET[char] * self.alpha) + self.beta) % Constants.N
            ciphertext.append(chr(encrypt_char + Constants.A_ORD))

        encrypted_text = "".join(ciphertext)
        return encrypted_text.upper()

    def decrypt(self):
        '''
         Function --
            Affine Cipher decryption of ciphertext
            x = a^-1 * (y - b) % 26
        Parameters --
        Returns --
            String, ciphertext
        '''
        inverse = pow(self.alpha, -1, Constants.N)
        print(inverse)

        ciphertext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        plaintext = []
        for char in ciphertext:
            decrypt_char = (
                (inverse * (Constants.ALPHABET[char] -
                            self.beta)) % Constants.N)

            plaintext.append(chr(int(decrypt_char) + Constants.A_ORD))

        decrypted_text = "".join(plaintext)
        return decrypted_text.upper()
