# https://github.com/coophalco 

import json, base64, os, sys, zlib, lzma, gzip, marshal
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
payload = json.loads('{"mode": "password", "salt": "G7zOvrgbT9iv4Xvb35mZFQ==", "kdf_iters": 200000, "nonce": "ClbyzEF2A+0t2oXw", "tag": "Kd12pgRXLdhDZmfIVne9lg==", "ciphertext": "ylhvr7Qxpiu/pYjLtAFn2nxsxrYu5dIDp4lD45iH11fj1AMYPXVLbMuK94pmtrM6ZY+1ADnQgYWQfl7tX1+bvueXpdJy2QIe425OEMf2Yd9LPhYmiHMjb2x39talvLmLqCA4GUnCPmZrzhgzumB9c0Ba3AvwmqIE7u2jH4Mg2DAagwowLfcfMrS3IieLYevyvFlu4BDiZqEVYX6cZjizSrqEBHGRWlrl2sG40QVCaFCbAj8tVhJuEz0hMwlZj1OdOji767gESdHC6g2yd1kr4uFdcK6h0SJ/pCF16zVPJnPhom1MBzrWJTjPWsu3G1QLkTX4hKj4878vtlFhsRXTwUjjCBjiSePOgA5VV3oy3X6IpRIjNMcD+CQwEmTKDqSVSI+wHD5aO3W4T9Anc+LBEay2UtioVxnnJJSZFKwBnW39LMwPB9DDmgZ201JyuA1kiTGfW2T/vn6u2t8KFI9pHBYG82FGFItokK0Of2FzXI6vDka/EDlVPTQfXUrmKpiLDyBplL+KNFdDVAus8Exj2iKY9QwYsVTlMJm4nEKx1hRBcVJRf7NQwZ5pwfo4VTAAyR8IzEzFIq0M8MOLEs78tK2SM7t9OKWxg9UZ4QdnW7PXKZhcBvqs2EMzuG0jDoQi3B3BbQyfK4TO6JxVBx2N+HH52U7h8lgnLsNoEJJfP0CwdiX5c1fFWsYtfRNbUkUqWSLPnNyEnrq53feB08XEuJGzQrNroS7YN2q5XwKAwiEyXmd7WcZPfKjr0QdY0z5MH1MZaziJcNcAo8bLcDfp7F7uvovRy0J3ySzhSa6cOLyfUNWembLtf11ORbAQt89Ei5obClp2pODWx0jni0c5Dj/3usqJ1WiIfo1SH9BCL2TMhDT7n9hSjlEIClFYm2BO4hBdaq4w2FgeJpjB2m5nHAZOnh0kqfA9TXC0XdcsKgpcNNeUqzAR8XkD+xf5VtOXtDnJxFv2DrzERwBeb6HQ3bZzdKP3pnU4K7MISfYwTD091iS4gljP0AOVT5Iu1rmZAp2lXtEmaGjY5mslTp3PaJ11AuGVsUVStD04qohqxo8uFleF+tY0oKcH3IiDTt473Tg3RGC0dEf3jJtg0m+G1rc0wMYTfnJ3UTBdkzXx3MlkkzDW4WTQ1P3Nv4T6KkVuEn156oJe1qL6GEOidysWdI6e0QOMWdhYOQ9jneRHBZXqzZl8wwkALbaGFAGSPIeStjVMEkdPw2e6Ya2K++QsZfzemI1ZX6LEEuCw88TzmowIIWEEid+Vx1g/apB8K1jrPKxo1ygxcIONwhKKOcuPRHBcZhPIizme2nN0PwuNJGBfPzyCO0uZus65A3dctopAfkvxBxuFmArtgRFM6wsPZiCSKF4Oy77mjBesDYgFWD27p5Kk7X2bfbfUVfdlyqHiDjLK1EsYLWDRLNNLowpY8762+YxUQh2EVyXhCMJ7BNM6ROH3ajOOIizZMvC9LQBB4o6CsTWet7kJAMbxeJifxkFbIHntiHns0zo6aW0qLy7TYZAK4RufL/pC3H61utOOJF6LAmj42bxJuB/aOBhQatYuM54JoDfqkJUGLgVxWb5P4VlVw/dA/meNqFdJk2LFsXm8oBs76yLiz8q7KlvFx3X+evitQbeFsqNNgGKNd40Nn5Ba2QnTixAnSIp1otMsb7NhqtJG5UH08d76a8xAU4pG8gtI0E/+r5TwqmDDSDcG98235f5TtfW6LPDeGumFinUUiNxFXQpjI7CqklrJ1wKSuByfs/h7G50uHyi2CzjuQm9SE8bE2Av1xl8eKSh16dtGu//eMpREPZeG3e2aL5Cs5+Nl7mKZ+PDMMB4vALtvFXarnZFcWK/T1yOMvMXA2ucf/8JR/9P0UlHPo1G6rXaSWIFe0V7hVuoomjmh9axl2ml3yv0vb2+C8oFuNDpCtej908ebQOgLxVzQ0Wf0rVFxmhnN9AFmrgxbvqyzKIU2n5DrCeAYO0oUh5cTUeNGMTcyz2ESErfSE9mmvdAJVYgqvsTQlbTWko505kWU/fJIC0HmgOp4QYEB4OMSFi2iUJcnhWssJuHxuaZMnMQ/3ZUJxdiVFX6FDVK3YtkqpJS5IVOOQh2vpVR89Q==", "wrapped_key": "nxajPjqzvjOy3nwd+pL6c2JzwiG0AsXoNSjjaPOquMM=", "wrap_nonce": "FU+56y30RVRsxcWo", "wrap_tag": "zUWPe84ulZWoB5ktTEyuVg=="}')
if payload.get("mode") != "password":
    print("Bad payload")
    sys.exit(1)
salt = base64.b64decode(payload["salt"])
iters = int(payload["kdf_iters"])
nonce = base64.b64decode(payload["nonce"])
tag = base64.b64decode(payload["tag"])
ciphertext = base64.b64decode(payload["ciphertext"])
wrapped_key = base64.b64decode(payload["wrapped_key"])
wrap_nonce = base64.b64decode(payload["wrap_nonce"])
wrap_tag = base64.b64decode(payload["wrap_tag"])
parts = ['PQ==', 'Umhj', 'bHRt', 'SkpX', 'T1VG', 'WW01', 'Qmhu', 'NUph', 'R1kz', 'R21O', 'MUpI', 'MXRF', 'Qlcy', 'VW5w']
rejoined = ''.join(parts[::-1])
step1 = base64.b64decode(rejoined)
step2 = base64.b64decode(step1)
pk = bytes([b ^ 42 for b in step2]).decode()
if isinstance(pk, str):
    pk = pk.encode()
kek = PBKDF2(pk, salt, dkLen=32, count=iters, hmac_hash_module=SHA256)
wrap_cipher = AES.new(kek, AES.MODE_GCM, nonce=wrap_nonce)
key = wrap_cipher.decrypt_and_verify(wrapped_key, wrap_tag)
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
exec(marshal.loads(gzip.decompress(lzma.decompress(zlib.decompress(cipher.decrypt_and_verify(ciphertext, tag))))), globals())
