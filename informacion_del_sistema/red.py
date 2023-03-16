import socket
import urllib.request

def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor

def public_ip():
    lista = '0123456789.'
    ip = ''
    dato = urllib.request.urlopen('http://checkip.dyndns.org').read()
    for x in str(dato):
        if x in lista:
            ip += x
    return ip

print('Red'.center(50, '-'))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
print(f'IP Local: {s.getsockname()}')
print(f'IP Equipo: {socket.gethostbyname(socket.gethostname())}')
s.close()
print(f'IP pública: {public_ip()}')