import string


class Shift:

    def __init__(self, text, key):
        self.text = text
        self.key = key

    def encrypt(self):
        N = 26
        a_ord = ord('a')

        self.text = self.text.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []
        for char in self.text.lower():
            char_to_ord_shifted = ((ord(char) - a_ord) + int(self.key)) % N
            ord_to_ciphertext = chr(char_to_ord_shifted + a_ord)
            ciphertext.append(ord_to_ciphertext)

            encrypted_text = "".join(ciphertext)
        return encrypted_text

    def decrypt(self):
        N = 26
        a_ord = ord('a')

        ciphertext = ciphertext.translate(
            str.maketrans("", "", string.whitespace))

        plaintext = []
        for char in ciphertext.lower():
            char_to_ord_shifted = (ord(char) - (int(self.key) + a_ord)) % N
            ord_to_plaintext = chr(char_to_ord_shifted + a_ord)
            plaintext.append(ord_to_plaintext)

        decrypted_text = "".join(plaintext)
        return decrypted_text

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
