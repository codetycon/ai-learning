from copy import deepcopy, replace
from dataclasses import dataclass, replace
from typing import List

@dataclass
class User:
    id: int
    name: str
    age: int
    skills: List[str]
#The same list is reused across function calls because default arguments are evaluated once, when the function is defined, not each time it’s called.

def add_messages(message, history=None):
    if history is None:
        history = []
    history.append(message)
    return history


def show_msg_history(msg='Hi'):
    return msg

print(add_messages("Hello"))
print(add_messages("How are you?"))
print(add_messages("What's up?"))


print(show_msg_history("What's up?"))
print(show_msg_history())




a = [1, 2, 3]
b = a

print(a is b)  # True, both a and b refer to the same list object
print(a == b)  # True, the contents of the lists are equal



c = [1, 2, 3]
print(a is c)  # False, a and c refer to different list objects
print(a == c)  # True, the contents of the lists are equal



a.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4], b is still referring to the same list object as a
print(c)  # [1, 2, 3], c is unaffected because it refers to a different list 


print("Using copy() and list() to create new list objects:")

d = a.copy();
e = list(a);

print(d is a)  # False, d is a new list object
print(e is a)  # False, e is a new list object
print(d == a)  # True, the contents of the lists are equal
print(e == a)  # True, the contents of the lists are equal

print(d);
print(e);

a.append(5);
print(a)  # [1, 2, 3, 4, 5]
print(d)  # [1, 2, 3, 4], d is unaffected because it refers to a different list
print(e)  # [1, 2, 3, 4], e is unaffected because it refers to a different list


print("Using copy() to create a new list object with dictionaries:")

f = [
    {
        "name": "Alice",
        "age": 30,
    }
]

g = f.copy();
print(f is g)  # False, g is a new list object
print(f == g)  # True, the contents of the lists are equal
print(f);
print(g);

print("Modifying the dictionary inside the original list:")
f[0]["age"] = 31;
print(g is f)  # False, g is still a different list object
print(g == f)  # True, the contents of the lists are equal

print(f)  # [{'name': 'Alice', 'age': 31}]
print(g)  # [{'name': 'Alice', 'age': 31}], g is affected because it refers to the same dictionary object inside the list


print(g[0] is f[0])  # True, both g and f refer to the same dictionary object inside the list
print(g[0] == f[0])  # True, both g and f refer to the same dictionary object inside the list



print("Using deepcopy() to create a new list object with dictionaries:")


h = deepcopy(f);
print(f is h)  # False, h is a new list object
print(f == h)  # True, the contents of the lists are equal
print(f);
print(h);

print("Modifying the dictionary inside the original list:")
f[0]["age"] = 32;
print(h is f)  # False, h is still a different list object
print(h == f)  # False, the contents of the lists are not equal anymore
print(f)  # [{'name': 'Alice', 'age': 32}]      
print(h)  # [{'name': 'Alice', 'age': 31}]

print(h[0]["name"] == f[0]["name"])  # True, both h and f have the same dictionary values inside the list
print(h[0]["name"] is f[0]["name"])  # True, Python interns identical strings, so both refer to the same string object in memory
print(h[0]["age"] == f[0]["age"])  # False, the age values are different (31 vs 32)


print("Using replace() to create a new dataclass object with modified attributes:")
a_user = User(id=1, name="Kishor Patidar", age=29, skills=["Python", "JavaScript", "Machine Learning"])
print(a_user);
new_user = replace(a_user, age=30);
print(new_user);



print("Task 1: Observe whether the original object changes.")
user = User(id=1, name="Kishor Patidar", age=29, skills=["Python", "JavaScript", "Machine Learning"]);
totalSkills = len(user.skills);
def update_user_skills(user, skill):
    user.skills.append(skill);


update_user_skills(user, "Data Science");
totalSkillsAfterUpdate = len(user.skills);
if totalSkillsAfterUpdate > totalSkills:
    print("The original object has changed.");



print("Task 2: Create a new Assignment, Shallow COpy and Deep Copy. Then print them");
original = [
    {
        "name": "Alice",
        "age": 30
    }
]

assignment = original;
shallow_copy = original.copy();
deep_copy = deepcopy(original);
print("Original:", original);
print("Assignment:", assignment);
print("Shallow Copy:", shallow_copy);
print("Deep Copy:", deep_copy);



print("Task 3: Predict answer.");
a = []

b = a

b.append(1)

print(a)
print(b)
print(a is b)