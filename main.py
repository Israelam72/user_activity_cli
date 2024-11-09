import typer
import json
import requests
from typing_extensions import Annotated


def main():
    username: Annotated[str, typer.Argument(help="The user name to get activity from")] = typer.prompt("Username")
    headers = {'Accept': 'application/json'}
    end_point = f"https://api.github.com/users/{username}/events"
    
    test = requests.get(end_point, headers=headers)
    print(test.json())

if __name__ == "__main__":
    typer.run(main)

"""
- Verificar como o json está chegando
- arrumar o json pra ficar legivel
- estudar para ver se é possivel adicionar class
"""