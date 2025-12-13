# https://github.com/coophalco 

import json, base64, os, sys, zlib, lzma, gzip, marshal
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
payload = json.loads('{"mode": "password", "salt": "DgFK4OqZ1wpj/g8wSFVA9w==", "kdf_iters": 200000, "nonce": "x9kRSfQtnsKyDYes", "tag": "OFxV8Kut4szA8fMqc1kGgg==", "ciphertext": "lA2qVG1JvNKtENJbiYinUh35CWPGwUbl6g96zCaVj0AW07QJ/BgThHuINuPZqNvTxgXaUPVqfCV87HC7X0FhodnsiK3LcvMjMA8I3PbBOruQv9ch3fFdhvPF6c1fKp0sSrrt8y1pos41XZUOgfsXIQOvHkG48F58lw9lJIg1JxioEDmHQ7qFQt+WQiVWuYtNExMMWuLJ46785goHrddBhzCoCvpG/DP78H29aBMnzlsAJkh4WLf+ka+OnRi3oADfl7VgMvu0WAaKqqdVgqq2eiKBBpiSFK5iUDgWM3iiQAKzKFsB4gqYFIeNJ5ZYb5y2vm66i78K/KbOsSmbUVrA2TV7Zs0gkFpAbP555YwB4YMw7pI1TF8ZsCHhPHqoKr1upBw0BuQQyUA5CCpjqM1DOJNW3EtyppscqqQZ36Nu893en++tNxsHvvaPfWLX6ts3FqwOfCWcchRoXGDObxt8iQVSIZgTax9Z/XAywnY33YIyHWGCgo7TC7Twi3GQGOfb2YDc0NT++e9fi5K8lRWZel3TBzzeFV6aPRExeMU7ap8v4aaO5ysLKtjQoi3NYM7h72qvqYt/bbOypj3HP18MRX8ZQCbk7lQqXpxMRba3xKHdZAx/UBoYzVI0v2JMpVSQUpyUNh8O6lzj7uKpui5EmUJAIdh1dafsM8j87dIimQKZp1S0ftFRnCDpvC5GksiyAtGTkP4DtYYerdmVzrF3DOlX1h3Onn3V+lKcOFDzO8KO8TZ5cgXDmwH+tzphSz44CJnFaICZda/A6sH7MVXQ1H345tx08H8zUuE3ac2Kkk7A+L8xvByRoWvlkzAbS0m7T405KBucZkNs1amIZPKYnCvoC48h5GsrHLjF7lxR+hfaGOAsUg0Oz5AvItT483kHcfkvWqAhMOEKstfsCpBKbbpENKD+UvHkyRheMg6Auf8AQoGQNeB0R46D1oQLnXBTrAMhSvtEOhkuJc7qCb0yda1764LRLegVVVKGTmsMF3UQEJDcJaZOvMNot/ThrTEA9INC2P7N9tcEYgSWwvOy5lKLt557cQ6SkGNlFdPaTgYEl/w/5FURun/Qw3m2NjP+N8xhxtad3AcaKrFgGYYrAa/MPlGuPb2tY8Yj7H4GDfotH9gLqn22+pdXB2G8F9OP9Tyu1dZJChPhkpqZ5gQLezrOORJZ8uY=", "wrapped_key": "dUKuwdIfwXpMvhTseOh1O44jkqNm1BWIrma+VnqApu4=", "wrap_nonce": "qgqsgtzKvpgEOn1E", "wrap_tag": "HpwEMPzhr9dFLk2fDABrNQ=="}')
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
