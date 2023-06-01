Primero creamos el archivo setup.py en la raiz de nuestro paquete

```
from setuptools import setup
setup(
    name="mipaquete",
    version="1.0",
    description="Mi paquete de ejemplo",
    author="Javier Portales",
    author_email="hey@javierportales.com",
    url="https://javierportales.com",
    packages=['mipaquete','mipaquete.numerouno','mipaquete.numerodos']
)
```

```
python setup.py sdist
```
Esto crea una carpeta dist y dentro un archivo comprimido, este archivo es el que debemos compartir
Para instalarlo
```
pip install dist\mipaquete-1.0.tar.gz
```
Para eliminarlo
```
pip uninstall mipaquete
```