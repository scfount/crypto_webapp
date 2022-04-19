from ciphers.decryption import Decryption
from ciphers.hack_vigenere_key import HackVigenereKey
from ciphers.shift import Shift
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

        plaintext = self.text

        ciphertext = []

        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                encrypt_char = (Constants.ALPHABET[plaintext[i]] +
                                Constants.ALPHABET[self.key[(i % len(self.key))]]) % Constants.N
                ciphertext.append(chr(encrypt_char + Constants.A_ORD))
            else:
                ciphertext.append(plaintext[i])

        encrypted_text = "".join(ciphertext)
        return encrypted_text

    def decrypt(self):
        '''
        Function --
        Parameters --
        Returns --
            String, plaintext
        '''
        ciphertext = self.text

        plaintext = []
        for i in range(len(ciphertext)):
            if ciphertext[i].isalpha():
                decrypted_char = (
                    Constants.ALPHABET[ciphertext[i]] - Constants.ALPHABET[self.key[(i % len(self.key))]]) % Constants.N
                plaintext.append(chr(decrypted_char + Constants.A_ORD))
            else:
                plaintext.append(ciphertext[i])

        decryption = Decryption("".join(plaintext), self.key)
        return [decryption]

    def decrypt_no_key(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        key_hacker = HackVigenereKey()

        possible_key_lengths = key_hacker.hack_key(self.text)

        decryptions = []
        # decrypt with best key length
        if len(possible_key_lengths) == 1:
            self.key = key_hacker.guess_key(self.text, possible_key_lengths[0])
            decryption = self.decrypt()
            decryptions.append(decryption[0])

            return decryptions
        else:
            # decrypt with most likely key lengths
            for possible_len in possible_key_lengths:
                self.key = key_hacker.guess_key(self.text, possible_len)
                decryption = self.decrypt()
                decryptions.append(decryption[0])

            return decryptions
