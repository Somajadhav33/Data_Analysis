#Creating Functions
def greet():
    print("Hello!")  #Function Definition/Body

greet() #Calling the Functions

# Function Vs Methods - when functions are written in the class then they are called methods

#Returning Values from Functions
def sum(a, b):
    return a + b

print(sum(10, 20))

# returnning Multiple values from function

def multiple_values():
    return 1, 2, 3, 3

a, b, c, d = multiple_values()
print(a, b, c, d)
e = multiple_values()
print(type(e))
print(e)


#Returnning List

def returnList():
    return [1, 2, 3, 4, 5]

print(returnList())

#Formal And Actual Arguments

def add(a, b): #formal arguments
    return a + b

print(add(10, 20)) #actual arguments

#Positional Arguments
def Positional_Args(name, age):
    print(name, age)

Positional_Args("John", 30) #Positional Arguments - correct order
Positional_Args(30, "John") #Positional Arguments - incorrect order


    