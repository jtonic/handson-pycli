from typing import List, Optional
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


class User(BaseModel):
    name: str
    age: int
    married: Optional[bool]
    children: List[str] = []
    friends: List[Person] = []


user_data = {
    "name": "Liviu Pazargic",
    "age": 51,
    "married": True,
    "children": ["Ligia", "Lara"],
    "friends": [{"name": "Tony", "age": 51}],
}

user = User(**user_data)

print(f"User name: {user}")
print(f"User details: {user.dict()}")
