from flask import request
from flask_restful import Resource


class AffineDecrypt(Resource):
    def post(self):
        ciphertext = request.json['ciphertext']
        alpha = int(request.json('alpha'))
        beta = int(request.json('beta'))
        inverse = (1/alpha)
        N = 26
        A_ORD = 97
        ALPHABET = {chr(i + A_ORD): i for i in range(N)}

        plaintext = []
        for char in ciphertext.lower():
            decrypt_char = inverse * (ALPHABET[char] - beta)
            plaintext.append(chr(decrypt_char + A_ORD))

        decrypted_text = "".join(plaintext)
        return {
            'resultStatus': 'SUCCESS',
            'decryption': decrypted_text
        }
