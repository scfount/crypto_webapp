from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from api.ciphers_API import ShiftDecryptNoKey, ShiftEncrypt, ShiftDecrypt, AffineEncrypt, AffineDecrypt, VigenereDecryptNoKey, VigenereEncrypt, VigenereDecrypt


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


api = Api(app)
resource_map = (
    (ShiftEncrypt, '/shift_encrypt'),
    (ShiftDecrypt, '/shift_decrypt'),
    (ShiftDecryptNoKey, '/shift_decrypt_no_key'),
    (VigenereEncrypt, '/vigenere_encrypt'),
    (VigenereDecrypt, '/vigenere_decrypt'),
    (VigenereDecryptNoKey, '/vigenere_decrypt_no_key'),
    (AffineEncrypt, '/affine_encrypt'),
    (AffineDecrypt, '/affine_decrypt')

)
for resource, route in resource_map:
    api.add_resource(resource, route)
