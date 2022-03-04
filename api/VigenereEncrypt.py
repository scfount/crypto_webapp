from flask import request
from flask_restful import Resource


class VigenereEncrypt(Resource):
    def post(self):

        return {
            'resultStatus': 'SUCCESS',
            'cipherText': encrypted_text
        }
