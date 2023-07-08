# Biblioteca Python



## Entorno Virtual
Primero debemos instalar el paquete necesario para crear entornos virtuales
```
sudo apt install python3.10-venv
```

Primero debemos crear el entorno virtual, en este caso creamos el directorio ```.venv```
```
python3 -m venv .venv
```

Luego debemos activarlo
```
source .venv/bin/activate
```

Activar el entorno virtual cambiará el prompt de tu consola para mostrar que entorno virtual está usando

Para desactivar el entorno virtual, digita en el terminal
```
deactivate
```

## Instalar pip
```
sudo apt install python3-pip
```

Para ver la versión de pip que tenemos instalada ejecutamos
```
pip3 --version
```

## Listar paquetes instalados con pip
```
python3 -m pip list
pip list
```

# Actualizar paquetes con pip
```
pip install --upgrade pip
```

## Paquetes pip

-pylint ( https://pylint.org/ )
```
pip install pylint
```

- autopep8 ( https://pypi.org/project/autopep8/ )
```
pip install autopep8
```

- argparse ( https://docs.python.org/es/3/library/argparse.html )
```
pip install argparse
```

- xthml2pdf
```
pip install xhtml2pdf
```

- jinja2
```
pip install jinja2
```

- Pandas
```
pip install pandas
```

- openpyxl

```
pip install openpyxl
```

- xlrd para leer archivos excel
```
pip install xlrd
```

- psutil
```
pip install psutil
```

- pyjwt
Si no viene instalado por defecto
```
pip install pyjwt

```
Si no funciona eliminar primero jwt
```
pip uninstall jwt

```

- python-jose
No funciona con pyjwt (no recomendado)
```
pip install pip install python-jose
```
- suds
```
pip install suds
```

- mysql-connector-python
```
pip install mysql-connector-python
```

- psycopg2
```
sudo apt install python3-psycopg2
pip install psycopg2-binary
```

- tkinter
```
sudo apt install python3-tk
```

- PySide6
```
pip install PySide6
```