"""
Teacher module.
"""

from dataclasses import dataclass
import click

boo = "Boo"


@dataclass
class Teacher:
    first_name: str
    last_name: str

    def test_notebook_debugging(self):
        click.secho(message="How are you man?", fg="red", bold=True)
        print("nothing here in teacher")


class Teacher2:
    def __init__(self, name: str):
        self.name = name
