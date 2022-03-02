import string
from flask import request
from flask_restful import Api, Resource, reqparse


class ShiftEncrypt(Resource):
    def post(self):
        '''
        Method -- 
            encrypts plain text using shift cipher algorithm
        Parameters:
            plaintext
            shift key
        Returns:
            String, cipher text
        '''
        plaintext = request.json['plaintext']
        shift = request.json['shift']

        plaintext = plaintext.translate(
            str.maketrans("", "", string.whitespace))
        cipher_text = []
        for char in plaintext.lower():
            adjusted_ord = (ord(char) - ord('a')) + int(shift) % 26
            shifted_char = chr(adjusted_ord + ord('a'))
            cipher_text.append(shifted_char)

            cipherText = "".join(cipher_text)
        return {
            'resultStatus': 'SUCCESS',
            'cipherText': cipherText
        }
