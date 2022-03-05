import string


class Affine:

    def __init__(self, text, alpha, beta):
        self.text = text
        self.alpha = int(alpha)
        self.beta = int(beta)

    def encrypt(self):
        '''
        Function -- 
            Affine Cipher encryption of plaintext
            y = ax + b (mod 26)
        Parameters --
        Returns --
            Ciphertext
        '''
        N = 26
        A_ORD = 97
        ALPHABET = {chr(i + A_ORD): i for i in range(N)}

        plaintext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []
        for char in plaintext.lower():
            encrypt_char = ((ALPHABET[char] * self.alpha) + self.beta) % 26
            ciphertext.append(chr(encrypt_char + A_ORD))

        encrypted_text = "".join(ciphertext)
        return encrypted_text

    def decrypt(self):
        '''
        Decrypts ciphertext using the affine cipher algorithm
        Users provides all needed information: text, alpha, beta
        Returns a string, the plaintext
        '''
        inverse = (1/self.alpha)
        N = 26
        A_ORD = 97
        ALPHABET = {chr(i + A_ORD): i for i in range(N)}

        ciphertext = self.text.translate(
            str.maketrans("", "", string.whitespace))

        plaintext = []
        for char in ciphertext.lower():
            decrypt_char = inverse * (ALPHABET[char] - self.beta)
            plaintext.append(chr(decrypt_char + A_ORD))

        decrypted_text = "".join(plaintext)
        return decrypted_text
