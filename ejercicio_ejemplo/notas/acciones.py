import notas.nota as modelo
from rich.console import Console
from rich.table import Table
from rich import print

class Acciones:
    def crear(self, usuario):
        print(f"{usuario[1]} vamos a crear una nueva nota")
        titulo = input("Ingrese el título: ")
        descripcion = input("Ingrese el contenido: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print("guardado")
        else:
            print("no se ha guardao la nota")
    
    def mostrar(self, usuario):
        print(f"{usuario[1]} estas son sus notas")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        table = Table(title="Notas")
        table.add_column("Título", justify="left", style="cyan", no_wrap=True)
        table.add_column("Descripción", justify="left", style="blue")
        for nota in notas:
            table.add_row(nota[2], nota[3])
        console = Console()
        if table.rows:
            console.print(table)
        else:
            print("[bold yellow]No hay notas[/bold yellow]")
    
    def borrar(self, usuario):
        print(f"{usuario[1]} Borramos la nota")
        titulo = input("Ingrese el título de la nota: ")
        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print("[bold green]Nota borrada[/bold green]")
        else:
            print("[bold red]Nota no borrada[/bold red]")
