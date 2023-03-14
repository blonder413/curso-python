import pathlib

def main():
    ruta = pathlib.Path()

    for archivo in ruta.iterdir():
        print(archivo.suffix)   # ver extensiones de un directorio

    extensiones = {archivo.suffix for archivo in ruta.iterdir()}
    print(f'extensiones: {extensiones}')

if __name__ == '__main__':
    main()