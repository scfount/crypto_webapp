import string
from flask import request
from flask_restful import Resource


class AffineEncrypt(Resource):

    def post(self):
        '''
        Function -- 
            Affine Cipher encryption of plaintext
            y = ax + b (mod 26)
        Parameters --
            Plaintext
            alpha value
            beta value
        Returns --
            Ciphertext
        '''
        plaintext = request.json['plaintext']
        alpha = int(request.json('alpha'))
        beta = int(request.json('beta'))
        N = 26
        A_ORD = 97
        ALPHABET = {chr(i + A_ORD): i for i in range(N)}

        plaintext = plaintext.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []
        for char in plaintext.lower():
            encrypt_char = ((ALPHABET[char] * alpha) + beta) % 26
            ciphertext.append(chr(encrypt_char + A_ORD))

        encrypted_text = "".join(ciphertext)
        return {
            'resultStatus': 'SUCCESS',
            'cipherText': encrypted_text
        }
