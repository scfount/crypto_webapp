import string
from flask import request
from flask_restful import Resource


class ShiftEncrypt(Resource):
    def post(self):
        '''
        Method -- 
            encrypts plain text using shift cipher algorithm
            y = x + a (mod 26)
        Parameters:
            plaintext
            shift key
        Returns:
            String, cipher text
        '''
        plaintext = request.json['plaintext']
        shift = request.json['shift']
        N = 26
        a_ord = ord('a')

        plaintext = plaintext.translate(
            str.maketrans("", "", string.whitespace))

        ciphertext = []
        for char in plaintext.lower():
            char_to_ord_shifted = ((ord(char) - a_ord) + int(shift)) % N
            ord_to_ciphertext = chr(char_to_ord_shifted + a_ord)
            ciphertext.append(ord_to_ciphertext)

            encrypted_text = "".join(ciphertext)
        return {
            'resultStatus': 'SUCCESS',
            'cipherText': encrypted_text
        }
