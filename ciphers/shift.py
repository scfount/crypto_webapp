import string
from .constants import Constants


class Shift:

    def __init__(self, text, key) -> None:
        self.text = text.lower()
        self.key = int(key)

    def encrypt(self):
        '''
        Function -- 
            encrypts plaintext using shift cipher algo
            y = x + b % 26
        Parameters --
        Returns --
            String, ciphertext
        '''
        plaintext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []
        for char in plaintext:
            if plaintext.isalpha():
                encrypted_char = (
                    Constants.ALPHABET[char] + self.key) % Constants.N
                ciphertext.append(chr(encrypted_char + Constants.A_ORD))
            else:
                ciphertext.append(plaintext)

        encrypted_text = "".join(ciphertext)
        return encrypted_text.upper()

    def decrypt(self):
        '''
        Function -- 
            decrypts ciphertext using shift cipher algo
            x = y - b % 26
        Parameters --
        Returns --
            String, plaintext
        '''
        ciphertext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        plaintext = []
        for char in ciphertext:
            if ciphertext.isalpha():
                decrypted_char = (
                    Constants.ALPHABET[char] - self.key) % Constants.N
                plaintext.append(chr(decrypted_char + Constants.A_ORD))
            else:
                plaintext.append(ciphertext)

        decrypted_text = "".join(plaintext)
        return decrypted_text.upper()

# for unknown key decrypt

        # def decrypt(self):
        # N = 26
        # a_ord = ord('a')

        # ciphertext = ciphertext.translate(
        #     str.maketrans("", "", string.whitespace))

        # decryptions = {}
        # for key in range(N):
        #     plaintext = []
        #     for char in ciphertext.lower():
        #         char_to_ord_shifted = (ord(char) - (key + a_ord)) % N
        #         ord_to_plaintext = chr(char_to_ord_shifted + a_ord)
        #         plaintext.append(ord_to_plaintext)
        #     decryptions[key] = "".join(plaintext)
        # return {
        #     'resultStatus': 'SUCCESS',
        #     'decryptions': decryptions
        # }
