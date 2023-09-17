import typer

import crispy_guacamole

app = typer.Typer()


@app.command()
def version():
    print(f"Version: {crispy_guacamole.__version__}", end="")
