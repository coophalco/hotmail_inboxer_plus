# https://github.com/coophalco 

import json, base64, os, sys, zlib, lzma, gzip, marshal
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
payload = json.loads('{"mode": "password", "salt": "2M+CGFsMmBHtyteJU8M6Nw==", "kdf_iters": 200000, "nonce": "CdZ0SPLNztL0fGSQ", "tag": "QAD6LOo6KAtPR/y8JEBv5g==", "ciphertext": "emSs7LvMiUpD1lL7YAJ6GnxsuJyfLHB7YiUaB08U8JbkrhouJGlm5ZBK3DH3TNAzHVqMTlbRW9evN7itrmmj+cidKSUuP9FB89m6j/vB7AJ5ZKZz4Bll6gBRc+5/uN05Lm+T4N3rmdDQrvLIlYYOYpsJDNKhmSZT/BTE3tLDNXnvyqUwQmcH0md5dFjxAZG2vITjY827HCllgks9o+h2vX52VzAYhqsXnE5CYbTScGo/snAJpkOndEgunSASiPMm3Icb6IkRmpmYNimHev99MgglygrBjaUB7CkPnMH6sMx4+kbZE1KUNyDuY2C7qS8EEW+YECgmT9rBqXBcyu3BXD8RUp1Ip2QsGhaL7z+3wz/yjxSKCm0S3xGW2u//vCfbiIWl73gHSWysR5oBsRLuCOVSW467yQrgP/wth9AccCs3MiRQEexy+nChBzzMvlmuR271JFS1Ml5fW9QuZ7LagSj9butyQM8XRAfTGP2eRZ/9UzStrGJ7Cy+TRTl6SDg6t4Otpsb98X50/Q64x/YMmuZUSQGQ+wI4Any2YbYyc1/OpPXHv7nD/CMUE+BDzO2h5j25z0m2oQOu5v8Pu14TZVdniB68hU0tDzuNxeL4S6zYELHUcAgtRmntOeTrciNlZOP+Ljfri96r2y97UarVvQ5kMYVQpdFmIi4lKxobDjuJbjqw9OiHOj+pUbKiHmPXGF/B3FgKkd4CNGWT/nUFTRBy7p+RiEBFKX78b66b+f0sWEDN0v8JFDKr4m0m4ty5ltXq3SPEoUgSuuHabwE+GF6TFaGY3RbRjHPrA6uaYgUAWUgh+cbkZ4jA8i4YK67MXAqLRiwDp56aK0LNYC10e/2hkMOnPLvYkKrXtJzmw7PloZL9s0J2Cp4csN6de4yhCKa1tJklB9UwzmdbWrPdx7Fk3HOXPCBqluvxAKtpfC95PTvlEiAMprTt1ksEVbNkv2CRjtfyjyw9Q/Ke2pwHHTKoKB/RPU82xS5q4ud/Vci11JebCSE0QPX3YsG15cMv+i3w8KAJix2yhVye9EyPF+XizmMdB6VfTK0r1g8VwE+Wsa/TdqB7B/MI0u9VWpWWcJSl9b0Nd6bvq2Zsr7CSTnih/3G05XY2ApdsHNJHnBzM4r1y7LwwfbWcTY/M3F8KNssp8jELPGZ208U=", "wrapped_key": "gtKMJAiXbVaEgqR9joEhJckm5w/5u6E9Zln4Uy3V9DE=", "wrap_nonce": "TFgteGTLdIbly991", "wrap_tag": "aD67aeTcMRRhjUu1OKAVVw=="}')
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
