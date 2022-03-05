from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from api.CiphersAPI import ShiftEncrypt, ShiftDecrypt, AffineEncrypt, AffineDecrypt, VigenereEncrypt, VigenereDecrypt


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


api = Api(app)
resource_map = (
    (ShiftEncrypt, '/shift_encrypt'),
    (ShiftDecrypt, '/shift_decrypt'),
    (AffineEncrypt, '/affine_encrypt'),
    (AffineDecrypt, '/affine_decrypt'),
    (VigenereEncrypt, '/vigenere_encrypt'),
    (VigenereDecrypt, '/vigenere_decrypt')
)
for resource, route in resource_map:
    api.add_resource(resource, route)
