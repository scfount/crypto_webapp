from flask import request
from flask_restful import Resource


class VigenereDecrypt(Resource):
    def post(self):

        return {
            'resultStatus': 'SUCCESS',
            'decryption': decrypted_text
        }
