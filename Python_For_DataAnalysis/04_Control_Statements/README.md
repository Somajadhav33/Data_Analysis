# Control Structures in Python – Loops & Flow Control 

Control structures let you **control the flow** of your program — repeat code, skip parts, or stop early.

Think of them as traffic signals for your code!

## 1. Conditional Statements

```python
if condition:
    # do something
elif another_condition:
    # do something else
else:
    # if nothing matches
```

Now let’s dive into **loops** and **control keywords**.

## 2. Loops in Python

### `for` Loop – When You Know How Many Times

Use when you have a sequence (list, string, range, etc.)

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry
```

#### Common Patterns

```python
# Loop through numbers
for i in range(5):          # 0 to 4
    print(i)

for i in range(1, 6):       # 1 to 5
    print(i)

for i in range(0, 10, 2):   # Step by 2 → even numbers
    print(i)

# Loop through string
for char in "Python":
    print(char)
```

### `while` Loop – When You Don’t Know How Many Times

Runs as long as the condition is **True**

```python
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4
```

### Infinite Loop – Runs Forever (Until Stopped)

```python
# Careful! This runs forever
while True:
    print("Hello forever!")

# Or with for (less common)
for _ in iter(int, 1):  # Advanced trick
    print("Infinite")
```

**How to stop infinite loop?**  
Use `break` (see below) or Ctrl+C in terminal.

### Nested Loops – Loop Inside a Loop

```python
for i in range(3):          # Outer loop
    for j in range(2):      # Inner loop
        print(f"i={i}, j={j}")
# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# ...
```

Great for tables, grids, patterns!

```python
# Print multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # New line
```

## 3. Loop Control Statements

| Statement   | What It Does                                      | Example                                      |
|-------------|---------------------------------------------------|----------------------------------------------|
| `break`     | **Stop the loop immediately**                     | ```python
for i in range(10):
    if i == 5:
        break
    print(i)


# Prints 0 to 4 only
| `continue`  | **Skip the rest of this iteration**, go to next   |
 ```python
for i in range(6):
    if i == 3:
        continue
    print(i)


# Prints 0,1,2,4,5 (skips 3)

| `pass`      | **Do nothing** – placeholder                      | 
```python
for i in range(5):
    if i == 3:
        pass  # I'll add code later
    print(i)
# Prints all 0–4
``` |
| `return`    | **Exit the function** (and loop if inside one)    | Used in functions (see below)                |

## 4. `return` in Functions (Important!)

`return` stops the function and sends back a value.

```python
def add(a, b):
    return a + b  # Stops here and returns result

print(add(5, 3))  # 8
```

If inside a loop, `return` stops **both** the loop and the function.

```python
def find_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # Stops loop + function
    return None

print(find_even([1, 3, 4, 7]))  # Returns 4
```

## 5. Real-World Example – Menu System

```python
while True:
    print("\n=== Menu ===")
    print("1. Say Hello")
    print("2. Say Bye")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "3":
        print("See you!")
        break  # Exit the infinite loop
    else:
        print("Invalid! Try again.")
        continue  # Skip rest, ask again
```

## Points to Remember (Must Know!)

| Rule                                      | Why It Matters                             |
|-------------------------------------------|--------------------------------------------|
| Always increment in `while` loops         | Or you get infinite loop!                  |
| Use `for` when you know the count         | Cleaner and safer                          |
| Use `while True` + `break` for menus      | Common pattern in real apps                |
| `break` exits the **nearest** loop        | Important in nested loops                  |
| `continue` skips to next iteration        | Great for filtering                        |
| `pass` is better than empty block         | Python hates empty code blocks             |
| `return` stops everything in function     | Don't put code after return                |
| Avoid infinite loops in production        | They crash programs!                       |

### Quick Cheat Sheet

```python
# For loop
for item in sequence:
    # code

# While loop
while condition:
    # code

# Infinite loop
while True:
    # code
    if done: break

# Controls
break     → stop loop
continue  → skip this round
pass      → do nothing
return    → exit function
```
