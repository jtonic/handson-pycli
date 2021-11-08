"""
Teacher module.
"""

from dataclasses import dataclass


@dataclass
class Teacher:
    first_name: str
    last_name: str


class Teacher2:
    def __init__(self, name: str):
        self.name = name
