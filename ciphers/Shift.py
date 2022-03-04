import string


class Shift:

    def encrypt(plaintext, key):
        N = 26
        a_ord = ord('a')

        plaintext = plaintext.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []
        for char in plaintext.lower():
            char_to_ord_shifted = ((ord(char) - a_ord) + int(key)) % N
            ord_to_ciphertext = chr(char_to_ord_shifted + a_ord)
            ciphertext.append(ord_to_ciphertext)

            encrypted_text = "".join(ciphertext)
        return encrypted_text

# TODO: change for known key decryption
    def decrypt(ciphertext, key):
        N = 26
        a_ord = ord('a')

        ciphertext = ciphertext.translate(
            str.maketrans("", "", string.whitespace))

        decryptions = {}
        for key in range(N):
            plaintext = []
            for char in ciphertext.lower():
                char_to_ord_shifted = (ord(char) - (key + a_ord)) % N
                ord_to_plaintext = chr(char_to_ord_shifted + a_ord)
                plaintext.append(ord_to_plaintext)
            decryptions[key] = "".join(plaintext)
        return {
            'resultStatus': 'SUCCESS',
            'decryptions': decryptions
        }
