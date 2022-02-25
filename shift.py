
def shift_cipher_decrypt(cipherText):
    '''
        Method -- shift_cipher_decrypt
            decrypts ciphertext by trying all possible keys
        Parameters:
            cipher_text -- the ciphertext to decrypt
        Returns:
            dictionary, shift key : plaintext
    '''
    decryptions = {}
    for key in range(26):
        plain_text = []
        for char in cipherText:
            if char.isupper():
                adjusted_ord = (ord(char) - (key + ord('A'))) % 26
                shifted_char = chr(adjusted_ord + ord('A'))
            else:
                adjusted_ord = (ord(char) - (key + ord('a'))) % 26
                shifted_char = chr(adjusted_ord + ord('a'))
            plain_text.append(shifted_char)
        decryptions[key] = "".join(plain_text)
        print(decryptions)
    return decryptions


def rsa_decrypt(cipher):
    '''
        Method -- rsa_decrypt
            decrypts RSA with a 1:1 plain text to ciphertext space
        Parameters:
            cipher_text -- the ciphertext to decrypt
        Returns:
            a string, the decrypted cipher text
    '''
    N = 18721
    E = 25
    decryptions = {}
    plaintext = []
    for i in range(26):
        char = chr(i + ord('a'))
        decryptions[(i ** E) % N] = char
    for c in cipher:
        if c in decryptions.keys():
            plaintext.append(decryptions[c])

    str_plaintext = "".join(plaintext)
    return str_plaintext


def affine_decrypt(cipher_text):
    '''
        Method -- affine_decrypt
            decrypts affine with a knowledge of the alpha value
        Parameters:
            cipher_text -- the ciphertext to decrypt
        Returns:
            a dictionary with all the possible decryptions
            beta value : plaintext
    '''
    n = 26
    a = 9
    beta_decryptions = {}

    for beta in range(26):
        plain_text = []
        for c in cipher_text:
            cipher_num = (a * (ord(c) - (ord('a') + beta))) % n
            plain_char = chr(cipher_num + ord('a'))
            plain_text.append(plain_char)
        beta_decryptions[beta] = "".join(plain_text)

    return beta_decryptions


def main():
    AFFINE_CIPHERTEXT = "tcabtiqmfheqqmrmvmtmaq"
    print(affine_decrypt(AFFINE_CIPHERTEXT))


if __name__ == "__main__":
    main()


# SHIFT_CIPHER_TEXT = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
    # print(shift_cipher_decrypt(SHIFT_CIPHER_TEXT))

    # RSA_CIPHER = [365, 0, 4845, 14930, 2608, 2608, 0]
    # plain_text = rsa_decrypt(RSA_CIPHER)
    # print(plain_text)
