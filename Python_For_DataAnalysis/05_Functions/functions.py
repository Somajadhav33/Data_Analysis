from functools import reduce

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

#Keyword Arguments - you specify which argument goes to which parameter
def grocery(item, price):
    print(item, price)

grocery(item="Apple", price=20)
grocery(price=20, item="Apple")   

#Default Arguments
def add(a=10, b=20):
    return a + b

print(add())
print(add(15))
print(add(15, 25))

#Variable Length Arguments - used when you don't know how many arguments will be passed - accept multiple arguments as tuple

def convert_to_list(*args):
    return [args]
print(convert_to_list(1, 2, 3, 4, 5))

#Keyword Variable Length Arguments - accept multiple arguments as dictionary

def print_details(**kwargs):
    print("Candidate Name : ", kwargs["name"])
    print("Candidate Age : ", kwargs["age"])

print_details(name="John", age=30)

#Local and Global Variables
user_id = 101 #Global Variable - defined outside the function - Can Access inside the function

def user_details():
    user_id = 102 #Local Variable - defined inside the function - Can't Access outside the function
    print(user_id)

user_details()


#Global Keyword - used to modify global variable inside the function
count = 0
def increment():
    global count
    count += 1
    return count

increment()
print(count)
increment()
print(count)

#recursive function  - function calling itself - it is important to have a base case to stop the recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))


#Lambda Function - anonymous function - one line function

nums = [1, 2, 3, 4, 5, 6]

#map -> apply a function to all items in an iterable
squares = list(map(lambda x: x**2, nums))
print(squares)

#filter -> filter items based on a condition
evens = list(filter(lambda x: x%2 == 0, nums))
print(evens)

#reduce -> apply a function to all items in an iterable and return a single value
add_all = reduce(lambda x, y: x + y, nums)
print(add_all)

#Generators(using yield) - generators gives you one value at a time
def count_up_to(n):
    num = 1
    while num <= n:
        yield num #generator - stores one value at a time
        num += 1

print(tuple(count_up_to(10)))

#Decorators
def wrapper_function(original_function):
    def inner_function(): #inner function
        print("--start--")
        original_function() #function call
        print("--end--")
    
    return inner_function

@wrapper_function #decorator
def sy_hello(): #original function
    print("Hello!")
sy_hello()
@wrapper_function #decorator
def hello_python(): #original function
    print("pissssssss!")

hello_python()




  
