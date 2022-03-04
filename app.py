from flask import Flask, request, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from api.AffineDecrypt import AffineDecrypt
from api.ShiftDecrypt import ShiftDecrypt
from api.ShiftEncrypt import ShiftEncrypt
from api.AffineEncrypt import AffineEncrypt

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
    (AffineDecrypt, '/affine_decrypt')
)
for resource, route in resource_map:
    api.add_resource(resource, route)
