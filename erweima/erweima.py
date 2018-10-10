import hashlib
md5 = hashlib.md5()
md5.update(b'zhuzhengren')
print(md5.hexdigest())
sha = hashlib.sha3_512(b'sssssssssssssss').hexdigest()
print(sha)

import binascii
dk = hashlib.pbkdf2_hmac(hash_name='sha256',
                         password=b'bad_password34',
                         salt=b'bad_salt',
                         iterations=100010)
print(binascii.hexlify(dk))

from Crypto.Cipher import DES
