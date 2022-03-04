
from cmath import sqrt
import math


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


def rsa_find_D(E, N):
    lcm = 0
    end = math.ceil(math.sqrt(N))
    # find phi
    phi = None
    for p in range(end):
        for q in range(p, N):
            if p * q == N:
                phi = math.lcm((p-1), (q-1))
    # find D
    for d in range(phi):
        if (E * d) % phi == 1:
            return ('d is:', d)


def verify_sig():
    y1 = 20679
    y2 = 11082
    alpha = 5
    beta = 26379
    p = 31847
    x = 20543

    key = None
    print('Find key')
    for i in range(p):
        if (alpha ** i) % p == y1:
            key = i
            print('key = ', key)
            break

    print('verify y2')
    print('y2 =', y2)
    print((x * (beta ** key)) % p)
    print(y2 == (x * (beta ** key)) % p)


def bf_a():
    alpha = 5
    beta = 26379
    p = 31847

    print('brute forcing a...')
    for a in range(p):
        if (alpha ** a) % p == beta:
            print('a =', a)
            break


def main():
    bf_a()


if __name__ == "__main__":
    main()


# SHIFT_CIPHER_TEXT = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
    # print(shift_cipher_decrypt(SHIFT_CIPHER_TEXT))

    # RSA_CIPHER = [365, 0, 4845, 14930, 2608, 2608, 0]
    # plain_text = rsa_decrypt(RSA_CIPHER)
    # print(plain_text)
