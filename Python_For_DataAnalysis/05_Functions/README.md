# Functions in Python

**What is a Function?**
Think of a function as a **mini-program** inside your main program. It is a reusable block of code that does one specific job. Instead of writing the same code again and again, you write it once in a function and "call" it whenever you need it.

---

## 1. Basic Functions

### Defining & Calling
- **Definition**: Creating the function using `def`.
- **Calling**: Using the function by writing its name followed by parentheses `()`.

```python
def greet():                        # Defining the function
    print("Hello, World!")

greet()                             # Calling the function -> Prints: Hello, World!
```

### Parameters vs. Arguments
Many beginners get these mixed up. Here is the simple difference:
- **Parameter**: The **variable name** written inside the parentheses when you *define* the function. (It's like a placeholder).
- **Argument**: The **actual value** you send to the function when you *call* it.

```python
# 'name' is the PARAMETER (placeholder)
def greet(name):
    print(f"Hello, {name}!")

# "Shery" is the ARGUMENT (actual data)
greet("Shery")
```

### Default Values
You can give a parameter a "backup" value. If the user forgets to provide an argument, the function uses the backup.

```python
def introduce(name, age=18):        # age defaults to 18 if not provided
    print(f"I'm {name}, {age} years old")

introduce("Alex")                   # Uses default age -> I'm Alex, 18 years old
introduce("Shery", 21)              # Uses provided age -> I'm Shery, 21 years old
```

### Return Values
- **Printing**: Just shows text on the screen. You can't use that text for math or logic later.
- **Returning**: Gives the result back to the computer so it can be saved in a variable.

**Think of it like ordering food:**
- `print`: The waiter shows you the food but takes it away immediately.
- `return`: The waiter gives you the food so you can eat it.

```python
def add(a, b):
    return a + b                    # Gives the result back

result = add(10, 20)                # The result (30) is saved in 'result'
print(result)                       # Now we print the saved result
```

---

## 2. Advanced Argument Types

### Positional Arguments
The standard way. The first argument goes to the first parameter, the second to the second, and so on. **Order matters!**

```python
def show(a, b):
    print(a, b)

show(1, 2)                          # a gets 1, b gets 2
```

### Keyword Arguments
You specify which argument goes to which parameter by name. **Order does not matter.**

```python
show(b=2, a=1)                      # Safer! a still gets 1, b gets 2
```

### Variable-Length Arguments
What if you don't know how many arguments the user will send?

#### `*args` (Non-Keyword Arguments)
- Allows you to pass **any number** of arguments.
- Python collects them all into a **Tuple** (a list that cannot be changed).
- *Analogy*: Like a shopping bag where you can throw in as many items as you want.

```python
def add_all(*numbers):
    # 'numbers' becomes a tuple: (1, 2, 3, 4, 5)
    return sum(numbers)

print(add_all(1, 2, 3, 4, 5))        # Output: 15
```

#### `**kwargs` (Keyword Arguments)
- Allows you to pass **any number** of named arguments (key=value).
- Python collects them into a **Dictionary**.
- *Analogy*: Like filling out a form with many optional fields (Name, Age, City, etc.).

```python
def print_details(**info):
    # 'info' becomes a dictionary: {'name': 'Shery', 'age': 21}
    for key, value in info.items():
        print(f"{key}: {value}")

print_details(name="Shery", age=21)
```

---

## 3. Scope (Global vs. Local)

**Analogy:**
- **Global Variable**: Like the air conditioning in a **House**. Everyone in every room can feel it.
- **Local Variable**: Like a lamp in a **Bedroom**. Only people in that bedroom can see it.

```python
x = 10                              # Global (House)

def func():
    y = 5                           # Local (Bedroom)
    print(x)                        # Works! Bedroom can see House stuff.
    # print(y)                      # Works! Inside Bedroom.

func()
print(x)                            # Works!
# print(y)                          # ERROR! You are outside the Bedroom.
```

### The `global` Keyword
If you want to change a Global variable from inside a function, you must ask for permission using `global`.

```python
count = 0

def increment():
    global count                    # Permission to edit the global 'count'
    count += 1

increment()
print(count)                        # 1 (It actually changed!)
```

---

## 4. Special Function Types

### Recursive Functions
A function that **calls itself**. It's like a loop but without `while` or `for`.
*Warning*: It must have a stop condition, or it will run forever (Infinite Loop).

```python
def count_down(n):
    if n == 0:                      # Stop condition
        print("Blast off!")
    else:
        print(n)
        count_down(n-1)             # Calls itself with one less

count_down(3)                       # 3, 2, 1, Blast off!
```

### Lambda Functions
A short, one-line function that has no name. Useful for quick, simple math.
*Syntax*: `lambda input: output`

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# map → transform each
squares = list(map(lambda x: x**2, nums))        # [1,4,9,16,25]

# filter → keep some
evens = list(filter(lambda x: x%2==0, nums))     # [2,4]

# reduce → combine all
total = reduce(lambda x,y: x+y, nums)           # 15
```

### Generators (Using `yield`)
Normal functions return everything at once. Generators give you one value at a time.
*Benefit*: Saves huge amounts of memory when working with large data.

```python
def count_up_to(n):
    num = 1
    while num <= n:
        yield num                   # Pauses here and gives 'num'
        num += 1                    # Resumes from here next time

# It doesn't store 1,2,3,4,5 in memory all at once.
for number in count_up_to(5):
    print(number)
```

### Decorators
A way to modify a function without changing its code. Think of it like **gift wrapping** – the gift (function) is the same, but it looks different (has extra behavior) on the outside.

```python
def wrapper_func(original_func):
    def inner():
        print("--- Start ---")      # Extra behavior before
        original_func()
        print("--- End ---")        # Extra behavior after
    return inner

@wrapper_func                       # Apply the decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# --- Start ---
# Hello!
# --- End ---
```

---


*Updated: December 2025*
