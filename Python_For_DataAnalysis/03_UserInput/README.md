## 2.11 Taking User Input in Python

Getting input from users is essential for interactive programs.  
Python provides several ways — from basic to advanced!

### 1. `input()` – The Most Common Method

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**Key Points**:
- Always returns a **string**
- You must convert if you need numbers
- Optional prompt message

```python
age = int(input("Enter your age: "))        # Convert to int
marks = float(input("Enter marks: "))       # Convert to float
```

### 2. Taking Multiple Inputs in One Line

#### Method 1: Using `split()`

```python
# Two numbers
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

# Multiple values
x, y, z = [int(x) for x in input("Enter 3 nums: ").split()]
```

#### Method 2: List Comprehension

```python
numbers = [int(x) for x in input("Enter numbers: ").split()]
print(f"You entered: {numbers}")
```

#### Method 3: Custom Separator

```python
name, age, city = input("Name,Age,City: ").split(",")
print(f"{name} is {age} years old from {city}")
```


### 3. Safe Input with Validation

```python
# Safe integer input
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

age = get_int("Enter your age: ")
```

### 4. Real-World Examples

```python
# Student marks calculator
print("=== Student Grade Calculator ===")
name = input("Student Name: ").title()
marks = [int(x) for x in input("Enter 5 subject marks: ").split()]

if len(marks) != 5:
    print("Please enter exactly 5 marks!")
else:
    total = sum(marks)
    avg = total / 5
    grade = "A" if avg >= 90 else "B" if avg >= 70 else "C" if avg >= 50 else "F"
    
    print(f"\n{name}'s Report:")
    print(f"Total: {total}/500")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
```

### 5. Comparison Table

| Method                        | Speed      | Best For                          | Returns   |
|-------------------------------|------------|-----------------------------------|-----------|
| `input()`                     | Medium     | General use, beginners            | String    |
| `sys.stdin.readline()`        | Very Fast  | Competitive programming           | String    |
| `input().split()`             | Medium     | Multiple values                   | List[str] |
| `map(int, input().split())`   | Fast       | Multiple numbers                  | int       |
| `getpass.getpass()`           | Secure     | Passwords                         | String    |

---