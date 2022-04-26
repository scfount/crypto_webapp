from ciphers.decryption import Decryption
from ciphers.hack_vigenere_key import HackVigenereKey
from .constants import Constants
import pycld2 as cld2


class Vigenere:

    def __init__(self, text, key, key_length) -> None:
        self.text = text.lower()
        self.key = key.lower()
        self.key_length = self.check_key_len(key_length)

    def check_key_len(self, key_len):
        if key_len == None or key_len == "":
            return 0
        else:
            return int(key_len)

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

    def decrypt_no_key_given_length(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        key_hacker = HackVigenereKey()

        decryptions = self.get_decryptions(key_hacker, [self.key_length])

        reliable_decryptions = self.get_reliable_decryptions(
            decryptions)

        if reliable_decryptions:
            reliable_decryptions.sort(
                key=lambda d: d.decryption_score,  reverse=True)
            return reliable_decryptions
        else:
            decryptions.sort(key=lambda d: d.decryption_score,  reverse=True)
            return decryptions

    def decrypt_no_key_no_length(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        SCORE_THRESHOLD = 1000
        key_hacker = HackVigenereKey()

        possible_key_lengths = key_hacker.hack_key(self.text)

        decryptions = self.get_decryptions(key_hacker, possible_key_lengths)

        reliable_decryptions = self.get_reliable_decryptions(
            decryptions)

        reliable_decryptions.sort(
            key=lambda d: d.decryption_score,  reverse=True)

        while reliable_decryptions[0].decryption_score < SCORE_THRESHOLD:
            decryptions = self.get_decryptions(key_hacker, [1, 2, 3])

            reliable_decryptions = self.get_reliable_decryptions(
                decryptions)

        return reliable_decryptions

    def get_decryptions(self, key_hacker, possible_key_lengths):
        """_summary_

        Args:
            key_hacker (_type_): _description_
            possible_key_lengths (_type_): _description_
        """
        decryptions = []

        for possible_len in possible_key_lengths:
            possible_keys = key_hacker.guess_keys(self.text, possible_len)
            for key in possible_keys:
                self.key = "".join(key)
                decryption = self.decrypt()
                this_decryption = decryption[0]
                decryptions.append(this_decryption)
        return decryptions

    def get_reliable_decryptions(self, decryptions):
        """_summary_

        Args:
            decryptions (_type_): _description_

        Returns:
            _type_: _description_
        """
        reliable_decryptions = []

        for d in decryptions:
            isReliable, textBytesFound, details = cld2.detect(d.text)
            d.isReliable = isReliable
            d.details = details
            d.decryption_score = details[0][-1]

            if isReliable == True and not self.repeated_key(d.key):
                reliable_decryptions.append(d)
        return reliable_decryptions

    def repeated_key(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        i = (key+key).find(key, 1, -1)
        return False if i == -1 else True
