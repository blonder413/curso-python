import jwt
import time

# header.payload.signature
secreto = 'Blonder413'
ts = int(time.time())
token = jwt.encode({'id': 1, 'nombre': 'jonathan', 'time': ts},secreto,algorithm='HS256')
resuelto = jwt.decode(token, secreto, algorithms='HS256')
print('jwt'.center(50, '-'))
print('token'.center(50, '-'))
print(token)
print('resuelto'.center(50, '-'))
print(resuelto)