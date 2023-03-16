from jose import jwt
import time

'''
Requiere instalar jwt en lugar de pyjwt
pip install jwt
'''

print('jose'.center(50, '-'))

# header.payload.signature
secreto = 'Blonder413'
ts = int(time.time())
token = jwt.encode({'id': 1, 'nombre': 'jonathan', 'time': ts}, secreto, algorithm='HS256')
print('token'.center(50, '-'))
print(token)
resuelto = jwt.decode(token, secreto, algorithms='HS256')
print('resuelto'.center(50, '-'))
print(resuelto)