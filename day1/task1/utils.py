from json import dumps;
from dataclasses import asdict;

def print_user(user):
    print(f"ID: {user.id}")
    print(f"Name: {user.name}")
    print(f"Age: {user.age}")
    print("Skills:")
    for skill in user.skills:
        print(f"- {skill}")

def to_json(user): # I want to convert user into a JSON object  
    return dumps(asdict(user), indent=2)
    

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
   
