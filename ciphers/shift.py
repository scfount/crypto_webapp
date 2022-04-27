from ciphers.chi_squared import ChiSquared
from ciphers.decryption import Decryption
from .constants import Constants
import pycld2 as cld2


class Shift:
    """Represents a Shift object for encryption or decrption
    """

    def __init__(self, text, key) -> None:
        """Initializes a Shift object

        Args:
            text (String): The plaintext or ciphertext
            key (int): The shift amount to apply
        """
        self.text = text.lower()
        self.key = self.check_key(key)
        self.vigenere = False

    def check_key(self, key):
        """Checks the passed in key for validity

        Args:
            key (String): The shift value in String form

        Returns:
            int || None: int if valid otherwise None
        """
        if key.isnumeric():
            return int(key)
        else:
            return None

    def encrypt(self):
        """encrypts plaintext using shift cipher algo
            y = x + b % 26

        Returns:
            String: The text encrypted
        """
        plaintext = self.text

        ciphertext = []
        for char in plaintext:
            if char.isalpha():
                encrypted_char = (
                    Constants.ALPHABET[char] + self.key) % Constants.N
                ciphertext.append(chr(encrypted_char + Constants.A_ORD))
            else:
                ciphertext.append(char)

        encrypted_text = "".join(ciphertext)
        return encrypted_text

    def decrypt(self):
        """decrypts ciphertext using shift cipher algo
            x = y - b % 26

        Returns:
            list: A list containing the decryption. List needed for passing
            to frontend
        """
        ciphertext = self.text

        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                decrypted_char = (
                    Constants.ALPHABET[char] - self.key) % Constants.N
                plaintext.append(chr(decrypted_char + Constants.A_ORD))
            else:
                plaintext.append(char)

        decryption = Decryption("".join(plaintext), self.key)

        return [decryption]

    def decrypt_no_key(self):
        """Decrypts ciphertext without a key by trying all possible shift values
        and returning a list of all outcomes, ordered by most likely using 
        frequency analysis

        Returns:
            list: A list containing all possible decryptions for each shift value
        """
        ciphertext = self.text

        decryptions = []
        for key in range(Constants.N):
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

        chi_squared = ChiSquared()
        for decryption in decryptions:
            decryption.chi_squared = chi_squared.calculate_chi_squared(
                decryption)

        decryptions.sort()

        if not self.vigenere:
            reliable_decryptions = self.get_reliable_decryptions(decryptions)
            return reliable_decryptions
        else:
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

            if isReliable == True and not self.repeated_key(decryption.key):
                reliable_decryptions.append(decryption)
        return reliable_decryptions
