from ciphers.decryption import Decryption
from ciphers.hack_vigenere_key import HackVigenereKey
from .constants import Constants
import pycld2 as cld2


class Vigenere:
    """Represents a Vigenere objects for encryption or decrption
    """

    def __init__(self, text, key, key_length) -> None:
        """initialize a Vigenere object

        Args:
            text (String): the plaintext or ciphertext
            key (String): the key to encrypt/decrypt if provided
            key_length (int): the length of the key, used for decryption of unknown key
        """
        self.text = text.lower()
        self.key = key.lower()
        self.key_length = self.check_key_len(key_length)

    def check_key_len(self, key_len):
        """Check to see if key length was provided and convert to correct type

        Args:
            key_len (String || None || int): The length of the key

        Returns:
            int: The length of the key
        """
        return 0 if key_len == None or key_len == "" else int(key_len)

    def encrypt(self):
        """Encrypts a string of plaintext to ciphertext using the provided key
        following the Vigenere encryption method

        Returns:
            String: The plaintext encrypted
        """
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
        """Decrypts a string of ciphertext to plaintext using a provided key

        Returns:
            String: The ciphertext decrypted
        """
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
        """Decrypts a string of ciphertext to plaintext finding a key of 
        the user specified key length

        Returns:
            list: A list of the possible decryptions
        """
        key_hacker = HackVigenereKey()

        possible_keys = self.get_keys(key_hacker, [self.key_length])

        decryptions = self.get_decryptions(possible_keys)

        reliable_decryptions = self.get_reliable_decryptions(
            decryptions)

        reliable_decryptions.sort(
            key=lambda d: d.decryption_score, reverse=True)

        return reliable_decryptions if reliable_decryptions else decryptions

    def decrypt_no_key_no_length(self):
        """Decrypts a string of ciphertext to plaintext with unknown key and 
        key length values

        Returns:
            list: A list of the possible decryptions
        """
        key_hacker = HackVigenereKey()

        possible_key_lengths = key_hacker.get_key_lengths(self.text)

        possible_keys = self.get_keys(key_hacker, possible_key_lengths)

        decryptions = self.get_decryptions(possible_keys)

        reliable_decryptions = self.get_reliable_decryptions(
            decryptions)

        if not reliable_decryptions or \
                reliable_decryptions[0].decryption_score < Constants.SCORE_THRESHOLD:
            short_keys = self.get_keys(key_hacker, [1, 2, 3])
            decryptions.extend(self.get_decryptions(short_keys))

            reliable_decryptions = self.get_reliable_decryptions(
                decryptions)

        reliable_decryptions.sort(
            key=lambda d: d.decryption_score, reverse=True)

        if reliable_decryptions:
            return reliable_decryptions
        else:
            decryptions.sort(
                key=lambda d: d.decryption_score, reverse=True)
            return decryptions

    def get_keys(self, key_hacker, possible_key_lengths):
        """Generate a list of possible keys based on all possible key lengths

        Args:
            key_hacker (HackVigenereKey): A Vigenere key hacking object
            possible_key_lengths (list): a list of ints representing key lengths

        Returns:
            list: A list of Strings representing possible keys
        """

        all_possible_keys = []

        for possible_len in possible_key_lengths:
            possible_keys = key_hacker.guess_keys(self.text, possible_len)
            for key in possible_keys:
                all_possible_keys.append(key)

        return all_possible_keys

    def get_decryptions(self, possible_keys):
        """Generate a list of possible decryptions based on a specified key length

        Args:
            possible_keys (list): A list of Strings representing possible keys

        Returns:
            list: A list of the possible decryptions using the provided keys
        """
        decryptions = []

        for key in possible_keys:
            self.key = "".join(key)
            decryption = self.decrypt()
            this_decryption = decryption[0]
            decryptions.append(this_decryption)
        return decryptions

    def get_reliable_decryptions(self, decryptions):
        """Generates a list of only reliable decryptions using a python language
        detection library

        Args:
            decryptions (list): A list of all possible decryptions

        Returns:
            list: A list of only the reliable decryptions based on the detection library
        """
        reliable_decryptions = []

        for decryption in decryptions:
            isReliable, textBytesFound, details = cld2.detect(decryption.text)
            decryption.isReliable = isReliable
            decryption.details = details
            decryption.decryption_score = details[0][-1]
            decryption.language = details[0][0]

            if isReliable == True and not self.repeated_key(decryption.key) \
                    and decryption.language == Constants.ENGLISH and \
                decryption.decryption_score > Constants.SCORE_THRESHOLD:
                reliable_decryptions.append(decryption)
        return reliable_decryptions

    def repeated_key(self, key):
        """Checks to see if the key is repeating itself

        Args:
            key (String): The decryption key

        Returns:
            bool: True if repeated, otherwise False
        """
        i = (key+key).find(key, 1, -1)
        return False if i == -1 else True
