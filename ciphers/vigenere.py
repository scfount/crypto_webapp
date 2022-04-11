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
            if plaintext[i].isalpha():
                encrypt_char = (Constants.ALPHABET[plaintext[i]] +
                                Constants.ALPHABET[self.key[(i % len(self.key))]]) % Constants.N
                ciphertext.append(chr(encrypt_char + Constants.A_ORD))
            else:
                ciphertext.append(plaintext[i])

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
            if ciphertext[i].isalpha():
                decrypted_char = (
                    Constants.ALPHABET[ciphertext[i]] - Constants.ALPHABET[self.key[(i % len(self.key))]]) % Constants.N
                plaintext.append(chr(decrypted_char + Constants.A_ORD))
            else:
                plaintext.append(ciphertext[i])

        decrypted_text = "".join(plaintext)
        return decrypted_text.upper()

    def decrypt_no_key(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        ciphertext = self.text.translate(
            str.maketrans("", "", string.whitespace))
        # start with set key length? Then build to unknown?
        # create bag of letters based on key length
        # ex: ciphertext = abcxyz, key length = 3
        # bag 1 = ax, bag 2 = by, bag 3 = cz
        # run frequency analysis with shift, 25 times on
        # each bag to get most likely key value(s)
        # brute force all permutations using chi-squared and take
        # the best result
        return None
