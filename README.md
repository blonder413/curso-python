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

## Paquetes pip
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