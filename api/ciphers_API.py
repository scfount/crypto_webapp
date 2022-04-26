from flask import request
from flask_restful import Resource
from ciphers.vigenere import Vigenere
from ciphers.shift import Shift
from ciphers.affine import Affine
import json


class ShiftEncrypt(Resource):
    def post(self):
        plaintext = request.json['text']
        key = request.json['key']
        shift = Shift(plaintext, key)
        ciphertext = shift.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': ciphertext,
            'plaintext': None
        }


class ShiftDecrypt(Resource):
    def post(self):
        ciphertext = request.json['text']
        key = request.json['key']
        shift = Shift(ciphertext, key)
        if key == "":
            decryptions = shift.decrypt_no_key()
        else:
            decryptions = shift.decrypt()
        decryptions_JSON = json.dumps(
            [decryption.__dict__ for decryption in decryptions])
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': None,
            'plaintext': decryptions_JSON
        }


class VigenereEncrypt(Resource):
    def post(self):
        plaintext = request.json['text']
        key = request.json['key']
        key_length = len(key)
        vigenere = Vigenere(plaintext, key, key_length)
        ciphertext = vigenere.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': ciphertext,
            'plaintext': None
        }


class VigenereDecrypt(Resource):
    def post(self):
        ciphertext = request.json['text']
        key = request.json['key']
        key_length = request.json['key_length']
        vigenere = Vigenere(ciphertext, key, key_length)
        if key == "" and (key_length == None or key_length == ""):
            decryptions = vigenere.decrypt_no_key_no_length()
        elif key == "" and (key_length != None or key_length != ""):
            decryptions = vigenere.decrypt_no_key_given_length()
        else:
            decryptions = vigenere.decrypt()
        decryptions_JSON = json.dumps(
            [decryption.__dict__ for decryption in decryptions])
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': None,
            'plaintext': decryptions_JSON
        }


class AffineEncrypt(Resource):
    def post(self):
        plaintext = request.json['text']
        alpha = int(request.json['alpha'])
        beta = int(request.json['beta'])
        affine = Affine(plaintext, alpha, beta)
        ciphertext = affine.encrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': ciphertext,
            'plaintext': None
        }


class AffineDecrypt(Resource):
    def post(self):
        ciphertext = request.json['text']
        alpha = int(request.json['alpha'])
        beta = int(request.json['beta'])
        affine = Affine(ciphertext, alpha, beta)
        plaintext = affine.decrypt()
        return {
            'resultStatus': 'SUCCESS',
            'ciphertext': None,
            'plaintext': plaintext
        }
