
import string
from .constants import Constants


class Vigenere:

    def __init__(self, text, key) -> None:
        self.text = text.lower()
        self.key = key.lower()

    def encrypt(self):
        '''
        Function --
        Parameters --
        Returns --
            String, ciphertext
        '''

        plaintext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []

        for i in range(len(plaintext)):
            encrypt_char = (Constants.ALPHABET[plaintext[i]] +
                            Constants.ALPHABET[self.key[(i % len(self.key))]]) % Constants.N
            ciphertext.append(chr(encrypt_char + Constants.A_ORD))

        encrypted_text = "".join(ciphertext)
        return encrypted_text.upper()

    def decrypt(self):
        '''
        Function --
        Parameters --
        Returns --
            String, plaintext
        '''
        ciphertext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        plaintext = []
        for i in range(len(ciphertext)):
            decrypted_char = (
                Constants.ALPHABET[ciphertext[i]] - Constants.ALPHABET[self.key[(i % len(self.key))]]) % Constants.N
            plaintext.append(chr(decrypted_char + Constants.A_ORD))

        decrypted_text = "".join(plaintext)
        return decrypted_text.upper()
