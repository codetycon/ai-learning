from json import dumps;

def print_user(user):
    print(f"ID: {user.id}")
    print(f"Name: {user.name}")
    print(f"Age: {user.age}")
    print("Skills:")
    for skill in user.skills:
        print(f"- {skill}")

def to_json(user): # I want to convert user into a JSON object  
    dumps_user = dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
        "skills": user.skills
    }, indent=2)
    print(dumps_user);
    # want to serelize user into a JSON string and print it to the console.
    json_string = dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
        "skills": user.skills
    });
    print(json_string);
    

def devide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
   
