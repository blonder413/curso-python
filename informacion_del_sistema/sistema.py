import psutil
import multiprocessing
import platform
import sys

print(f'número de núcleos del CPU: {psutil.cpu_count()}')
print(f'número de núcleos del CPU: {multiprocessing.cpu_count()}')
print(f'Arquitectura: {platform.machine()}')
print(f'Arquitectura: {platform.architecture()}')
print(f'Tipo de plataforma: {platform.python_compiler()}')
print(f'Núcleo: {platform.release()}')
print(f'Host Name: {platform.node()}')
print(f'Tipo de kernel: {platform.platform()}')
print(f'Arquitectura: {platform.processor()}')
print(f'OS: {platform.system()}')
print(f'OS: {sys.platform}')
print(f'Versión OS: {platform.version()}')
print(f'Versión OS: {platform.uname()}')
print(f'Versión Python: {platform.python_version()}')
print(f'Versión Java: {platform.java_ver()}')