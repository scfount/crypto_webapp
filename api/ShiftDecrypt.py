from flask import request
from flask_restful import Api, Resource, reqparse


class ShiftDecrypt(Resource):
    def post(self):
        '''
        Method -- shift_cipher_decrypt
            decrypts ciphertext by trying all possible keys
        Parameters:
            cipher_text -- the ciphertext to decrypt
        Returns:
            dictionary, shift key : plaintext
        '''
        cipherText = request.json['text']
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
        return {
            'resultStatus': 'SUCCESS',
            'decryptions': decryptions
        }
