from ciphers.decryption import Decryption
from .constants import Constants
import pycld2 as cld2


class Affine:
    """Represents an Affine object for encryption/decryption
    """

    def __init__(self, text, alpha, beta) -> None:
        """Initializes an Affine object

        Args:
            text (String): The plaintext or ciphertext
            alpha (int): The alpha value
            beta (int): the beta value
        """
        self.text = text.lower()
        self.alpha = self.check_num(alpha)
        self.beta = self.check_num(beta)

    def check_num(self, n):
        """checks to see if n is a number

        Args:
            n (String or Int): the value to check

        Returns:
            None | Int: Int if number, otherwise None
        """
        return None if n == "" else int(n)

    def encrypt(self):
        """Affine Cipher encryption of plaintext
            y = ax + b % 26

        Returns:
            String: The encrypted text
        """
        plaintext = self.text
        ciphertext = []
        for char in plaintext:
            if char.isalpha():
                encrypt_char = (
                    (Constants.ALPHABET[char] * self.alpha) + self.beta) % Constants.N
                ciphertext.append(chr(encrypt_char + Constants.A_ORD))
            else:
                ciphertext.append(char)

        encrypted_text = "".join(ciphertext)
        return encrypted_text

    def decrypt(self):
        """Affine Cipher decryption of ciphertext
            x = a^-1 * (y - b) % 26

        Returns:
            String: The decrypted text
        """
        inverse = pow(self.alpha, -1, Constants.N)
        ciphertext = self.text

        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                decrypt_char = (
                    (inverse * (Constants.ALPHABET[char] -
                                self.beta)) % Constants.N)
                plaintext.append(chr(int(decrypt_char) + Constants.A_ORD))
            else:
                plaintext.append(char)

        decrypted_text = "".join(plaintext)
        key = "alpha: {alpha}, beta: {beta}".format(
            alpha=self.alpha, beta=self.beta)
        decryption = Decryption(decrypted_text, key)
        return [decryption]

    def decrypt_no_key(self):
        """Tries all possible affine keys

        Returns:
            list: A list of decryptions
        """
        decryptions = self.get_decryptions()

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

    def get_decryptions(self):
        """Generates a list of possible decryptions by trying all alpha
        and beta values

        Returns:
            list: a list of decryptions
        """
        decryptions = []

        for alpha in Constants.COPRIME:
            self.alpha = alpha
            for beta in range(27):
                self.beta = beta
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

            if isReliable == True and decryption.language == Constants.ENGLISH \
                    and decryption.decryption_score > Constants.SCORE_THRESHOLD:
                reliable_decryptions.append(decryption)
        return reliable_decryptions
