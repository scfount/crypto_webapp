from flask import request
from flask_restful import Resource
from ciphers.vigenere import Vigenere
from ciphers.shift import Shift
from ciphers.affine import Affine


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


class ShiftDecryptNoKey(Resource):
    def post(self):
        ciphertext = request.json['ciphertext']
        key = ""
        shift = Shift(ciphertext, key)
        plaintext = shift.decrypt_no_key()
        plaintext_JSON = []
        for text in plaintext:
            plaintext_JSON.append(text.toJSON())

        return {
            'resultStatus': 'SUCCESS',
            'plaintext': plaintext_JSON
        }


class VigenereEncrypt(Resource):
    def post(self):
        plaintext = request.json['plaintext']
        key = request.json['key']
        vigenere = Vigenere(plaintext, key)
        ciphertext = vigenere.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': ciphertext
        }


class VigenereDecrypt(Resource):
    def post(self):
        ciphertext = request.json['ciphertext']
        key = request.json['key']
        vigenere = Vigenere(ciphertext, key)
        plaintext = vigenere.decrypt()
        return {
            'resultStatus': 'SUCCESS',
            'plaintext': plaintext
        }


class VigenereDecryptNoKey(Resource):
    def post(self):
        ciphertext = request.json['ciphertext']
        key = ""
        vigenere = Vigenere(ciphertext, key)
        plaintext = vigenere.decrypt_no_key()
        return {
            'resultStatus': 'SUCCESS',
            'plaintext': plaintext
        }


class AffineEncrypt(Resource):

    def post(self):
        plaintext = request.json['plaintext']
        alpha = int(request.json['alpha'])
        beta = int(request.json['beta'])
        affine = Affine(plaintext, alpha, beta)
        ciphertext = affine.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': ciphertext
        }


class AffineDecrypt(Resource):

    def post(self):
        ciphertext = request.json['ciphertext']
        alpha = int(request.json['alpha'])
        beta = int(request.json['beta'])
        affine = Affine(ciphertext, alpha, beta)
        plaintext = affine.decrypt()
        return {
            'resultStatus': 'SUCCESS',
            'plaintext': plaintext
        }
