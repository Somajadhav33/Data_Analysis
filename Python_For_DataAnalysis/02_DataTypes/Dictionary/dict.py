#Creating Dict
person = { #keys Must Be immutable like string, tuple, frozanset
    "name" : "Soma",
    "age" : 21,
    "city" : "Sangli"
}
print(person)

student = dict(name="Alex", age=20, course="python")
print(student)

mixed_keys = {
    "string" : "hello",
    20 : "answer",
    (1, 2) : "tuple",
    frozenset({1, 2, 3}) : "frozanset"
}
print(mixed_keys)

# User profile
user = {
    "id": 101,
    "username": "soma",
    "is_active": True,
    "roles": ["student", "mentor"],
    "stats": {"posts": 50, "likes": 1200}
}


#methods and operations
#Access
print(len(user))
print(user["username"])
print(user.get("is_active", "N/A"))

#Modify
user["is_active"] = False #update
user["email"] = "soma@gmail.com" #add
user.update({"job": "Developer"})
print(user)

#Remove
del user["stats"]
print(user)

#Check
print("username" in user)
print(user.keys())
print(user.values())
print(user.items())

### Dictionary Comprehensions (Pythonic!)

squares = {x : x**2 for x in range(1,11)}
print(squares)

#Loop through dictionary

for key, value in user.items():
    print(f"{key} : {value}")