import hashlib
import os

password = '123456'

salt = str(os.urandom(10)).encode('UTF-8')
cifrado = hashlib.scrypt(password.encode('UTF-8'), salt=salt, n=2, r=8, p=1)

print(cifrado)
print(str(cifrado).encode('utf8'))
