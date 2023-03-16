import psutil

def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor

cpufreq = psutil.cpu_freq()
print(f'Núcleos Físicos: {str(psutil.cpu_count(logical=False))}')
print(f'Total núcleos: {str(psutil.cpu_count(logical=True))}')

print(f'Máxima frecuencia: {cpufreq.max:.2f}Mhz')
print(f'Mínima frecuencia: {cpufreq.min:.2f}Mhz')
print(f'Frecuencia actual: {cpufreq.current:.2f}Mhz')

for i, percent in enumerate(psutil.cpu_percent(percpu=True)):
    print(f'Núcleo {i}: {percent}%')
print(f'Tital CPU usado: {psutil.cpu_percent()}%')