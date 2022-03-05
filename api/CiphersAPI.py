from flask import request
from flask_restful import Resource
from ciphers.Shift import Shift


class ShiftEncrypt(Resource):
    def post(self):
        plaintext = request.json['plaintext']
        key = request.json['key']
        shift = Shift(plaintext, key)
        ciphertext = shift.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': ciphertext
        }


class ShiftDecrypt(Resource):
    def post(self):
        ciphertext = request.json['ciphertext']
        key = request.json['key']
        shift = Shift(ciphertext, key)
        plaintext = shift.decrypt()
        return {
            'resultStatus': 'SUCCESS',
            'plaintext': plaintext
        }
