from heapq import heapify
import string
from ciphers.chi_squared import Chi_Squared
from ciphers.decryption import Decryption
from .constants import Constants


class Shift:

    def __init__(self, text, key) -> None:
        self.text = text.lower()
        self.key = self.check_key(key)

    def check_key(self, key):
        if key.isnumeric():
            return int(key)
        else:
            return None

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
            if char.isalpha():
                encrypted_char = (
                    Constants.ALPHABET[char] + self.key) % Constants.N
                ciphertext.append(chr(encrypted_char + Constants.A_ORD))
            else:
                ciphertext.append(char)

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
            if char.isalpha():
                decrypted_char = (
                    Constants.ALPHABET[char] - self.key) % Constants.N
                plaintext.append(chr(decrypted_char + Constants.A_ORD))
            else:
                plaintext.append(char)

        decrypted_text = "".join(plaintext)
        return decrypted_text.upper()

    def decrypt_no_key(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        ciphertext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        decryptions = []
        for key in range(1, Constants.N):
            plaintext = []
            for char in ciphertext.lower():
                if char.isalpha():
                    decrypted_char = (
                        Constants.ALPHABET[char] - key) % Constants.N
                    plaintext.append(chr(decrypted_char + Constants.A_ORD))
                else:
                    plaintext.append(char)

            decryption = Decryption("".join(plaintext), key)
            decryptions.append(decryption)

        chi_squared = Chi_Squared(len(ciphertext))
        for decryption in decryptions:
            decryption.chi_squared = chi_squared.calculate_chi_squared(
                decryption)

        heapify(decryptions)
        for d in decryptions:
            print(d)

        return decryptions
