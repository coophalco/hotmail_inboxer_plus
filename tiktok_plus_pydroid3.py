# https://github.com/coophalco 

import json, base64, os, sys, zlib, lzma, gzip, marshal
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
payload = json.loads('{"mode": "password", "salt": "ds0oR3F+qKTwfXeayIPKEA==", "kdf_iters": 200000, "nonce": "OjQjHX6IzQJLfycm", "tag": "BOhaafaZxiNSylgaXvu8wg==", "ciphertext": "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", "wrapped_key": "RZARxcd7DHUBR/tIGwjhyG9pKhT84OdXCoP9hU0sQ+I=", "wrap_nonce": "wBEZ60nUI8gsto2q", "wrap_tag": "KqLdiDm4vmhc7I8XRib0dA=="}')
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
