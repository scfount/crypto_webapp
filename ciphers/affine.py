from .constants import Constants


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
        self.alpha = int(alpha)
        self.beta = int(beta)

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
        return decrypted_text
