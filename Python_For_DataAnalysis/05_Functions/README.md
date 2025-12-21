# Python Functions Guide

This document provides detailed definitions and explanations for every concept used in `functions.py`.

## 1. Core Concepts

### Function

**Definition**: A function is a block of organized, reusable code that performs a single, specific related action. It only runs when it is called.

- **Why use it?**: To avoid writing the same code over and over again.
- **Code**:
  ```python
  def greet():
      print("Hello!")
  greet()
  ```

### Function vs Method

**Definition**:

- **Function**: Defined independently (stand-alone).
- **Method**: A function that is defined inside a class and is associated with an object.

## 2. Returning Values

### Return Statement

**Definition**: The `return` statement is used to exit a function and go back to the place where it was called. It can send a result back to the caller.

- **Code**:
  ```python
  def sum(a, b):
      return a + b
  ```

### Returning Multiple Values

**Definition**: Python functions can return more than one value. When they do, Python automatically packs these values into a **Tuple**.

- **Code**:
  ```python
  def multiple_values():
      return 1, 2, 3
  # Returns: (1, 2, 3)
  ```

## 3. Arguments and Parameters

### Formal vs Actual Arguments

**Definition**:

- **Formal Arguments (Parameters)**: The variables written in the parenthesis when _defining_ the function. They act as placeholders.
- **Actual Arguments**: The real values passed to the function when _calling_ it.
- **Code**:
  ```python
  def add(a, b):      # 'a' and 'b' are Formal Arguments
      return a + b
  add(10, 20)         # '10' and '20' are Actual Arguments
  ```

### Positional Arguments

**Definition**: Arguments that must be passed in the correct order. The first argument goes to the first parameter, the second to the second, and so on.

- **Code**:
  ```python
  def user(name, age):
      print(name, age)
  user("John", 30) # Correct order
  ```

### Keyword Arguments

**Definition**: Arguments passed by specifying the parameter name. When using keyword arguments, the order does not matter.

- **Code**:
  ```python
  def grocery(item, price):
      print(item, price)
  grocery(price=20, item="Apple") # Order doesn't matter
  ```

### Default Arguments

**Definition**: Parameters that assume a default value if a value is not provided in the function call.

- **Code**:
  ```python
  def add(a=10, b=20):
      return a + b
  print(add())    # Uses default: 10 + 20
  print(add(5))   # Uses 5 + 20
  ```

## 4. Variable Length Arguments

### `*args` (Non-Keyword Arguments)

**Definition**: Special syntax used to pass a variable number of arguments to a function. It allows you to pass as many arguments as you want, and they are stored as a **Tuple**.

- **Code**:
  ```python
  def convert_to_list(*args):
      print(args)
  convert_to_list(1, 2, 3, 4, 5) # Output: (1, 2, 3, 4, 5)
  ```

### `**kwargs` (Keyword Arguments)

**Definition**: Special syntax that allows you to pass a variable number of _keyword_ (named) arguments. They are stored as a **Dictionary**.

- **Code**:
  ```python
  def print_details(**kwargs):
      print(kwargs)
  print_details(name="John", age=30) # Output: {'name': 'John', 'age': 30}
  ```

## 5. Variable Scope

### Local vs Global Variables

**Definition**:

- **Global Variable**: A variable declared outside all functions. It can be accessed by any function.
- **Local Variable**: A variable declared inside a function. It can only be used inside that specific function.

### The `global` Keyword

**Definition**: A keyword used to modify a global variable inside a local scope (inside a function). Without this keyword, modifying a global variable inside a function simply creates a new local variable with the same name.

- **Code**:
  ```python
  count = 0
  def increment():
      global count  # Allows proper modification of the global 'count'
      count += 1
  ```

## 6. Advanced Functions

### Recursive Function

**Definition**: A function that calls itself. To prevent it from running forever (infinite loop), it must have a "base case" that stops the recursion.

- **Example**: Calculating factorial (`5! = 5 * 4 * 3 * 2 * 1`).

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

### Lambda Function

**Definition**: A small, anonymous (nameless) function. It can take any number of arguments but can only have one expression.

- **Three common helpers**:
  1.  **Map**: Applies a function to every item in a list.
  2.  **Filter**: Creates a list of elements for which a function returns true.
  3.  **Reduce**: Performs a rolling computation to sequential pairs of values in a list (e.g., summing them all up).

**Example**:

```python
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

```

### Generators (`yield`)

**Definition**: A function that returns an iterator (a sequence of values) one by one using the `yield` keyword. Unlike a standard function that returns all values at once (and uses more memory), a generator produces values on the fly.

- **Benefit**: More memory efficient for large datasets.
  **Example**:

```python
def count_up_to(n):
    num = 1
    while num <= n:
        yield num #generator - stores one value at a time
        num += 1

print(tuple(count_up_to(10)))
```

### Decorators

**Definition**: A design pattern that allows you to modify the behavior of a function without changing its code. It "wraps" another function in order to extend its behavior.

- **Syntax**: Uses the `@` symbol (e.g., `@wrapper_function`).

**Example**:

```python
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
```

---

Last Updated \_ Dec 2025
