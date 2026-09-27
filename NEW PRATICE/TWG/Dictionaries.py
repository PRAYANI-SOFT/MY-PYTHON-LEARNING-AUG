course={}

person = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "city": None
}

NAME = {person["name"]: "kuller"}

print(NAME["John"])

print(NAME)
print(NAME,type(NAME),id(NAME))

NAME2=NAME.copy()

NAME.clear()
print(NAME,type(NAME),id(NAME))
print(NAME2,type(NAME2),id(NAME2))
NAME3=person.copy()
print(NAME3,type(NAME3),id(NAME3))
print(person,type(person),id(person))

NAME4=person.get("age")

print(NAME4,type(NAME4),id(NAME4))





