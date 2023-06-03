"""
typer muestra los errores en los print de forma colorida
"""
import typer


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
