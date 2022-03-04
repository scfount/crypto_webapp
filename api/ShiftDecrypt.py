import string
from flask import request
from flask_restful import Resource


class ShiftDecrypt(Resource):
    def post(self):
        '''
        Method --
            decrypts ciphertext by trying all possible keys
        Parameters:
            ciphertext
        Returns:
            dictionary, shift key : plaintext
        '''
        ciphertext = request.json['text']
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
