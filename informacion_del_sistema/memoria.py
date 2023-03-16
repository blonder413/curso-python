import psutil

def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor

svmem = psutil.virtual_memory()
print(f'Total: {get_size(svmem.total)}', end=' | ')
print(f'Disponible: {get_size(svmem.available)}', end=' | ')
print(f'Usada: {get_size(svmem.used)}', end=' | ')
print(f'Porcentae: {svmem.percent}%')

swap = psutil.swap_memory()
print(f'Total: {get_size(swap.total)}', end=' | ')
print(f'Disponible: {get_size(swap.free)}', end=' | ')
print(f'Usada: {get_size(swap.used)}', end=' | ')
print(f'Porcentae: {swap.percent}%')