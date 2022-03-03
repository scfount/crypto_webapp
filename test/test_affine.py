# from flask import json
# from app import app


# def test_affine_encrypt():
#     response = app.test_client.post(
#         '/affine_encrypt',
#         data=json.dumps({'plaintext': 'a', 'alpha': '3', 'beta': '1'}),
#         content_type='application/json',
#     )
#     data = json.loads(response.get_data(as_text=True))
#     assert response.status_code == 200
#     assert data['cipherText'] == 'b'
