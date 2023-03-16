import psutil

def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor

partitions = psutil. disk_partitions()
''''
for partition in partitions:
    print(f'Dispositivos: {partition.device}', end=' | ')
    print(f'Puntos de montaje: {partition.mountpoint}', end=' | ')
    print(f'File system: {partition.fstype}')
'''
''''
for partition in partitions:
    print(f'Dispositivos: {partition.device}', end=' | ')
    print(f'Puntos de montaje: {partition.mountpoint}', end=' | ')
    print(f'File system: {partition.fstype}')
'''
for partition in partitions:
    try:
        particiones_usadas = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue

    if partition.mountpoint != '/' and partition.mountpoint != '/home':
        continue
    
    print(partition.mountpoint, end=' - ')
    print(f'Tamaño total: {get_size(particiones_usadas.total)}', end=' | ')
    print(f'En uso: {get_size(particiones_usadas.used)}', end=' | ')
    print(f'Libre: {get_size(particiones_usadas.free)}', end=' | ')
    print(f'Porcentaje: {particiones_usadas.percent}%')