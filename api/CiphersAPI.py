from flask import request
from flask_restful import Resource
from ciphers.Shift import Shift
from ciphers.Affine import Affine


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


class AffineEncrypt(Resource):

    def post(self):
        plaintext = request.json['plaintext']
        alpha = int(request.json('alpha'))
        beta = int(request.json('beta'))
        affine = Affine(plaintext, alpha, beta)
        ciphertext = affine.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': ciphertext
        }


class AffineDecrypt(Resource):

    def post(self):
        ciphertext = request.json['ciphertext']
        alpha = int(request.json('alpha'))
        beta = int(request.json('beta'))
        affine = Affine(ciphertext, alpha, beta)
        plaintext = affine.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'plaintext': plaintext
        }
