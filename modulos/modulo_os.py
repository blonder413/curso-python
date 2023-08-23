import os

ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)


def permisos():
    # Se recomienda usar try except cuando se trabaja con archivos
    os.chmod(ruta + "/typer.py", 0o664)


if __name__ == "__main__":
    permisos()
