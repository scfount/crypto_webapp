from flask_restful import Api, Resource, reqparse

class CryptoApiHandler(Resource):
    def get(self):
        return {
        'resultStatus': 'SUCCESS',
        'message': "Run the affine Cipher"
        }