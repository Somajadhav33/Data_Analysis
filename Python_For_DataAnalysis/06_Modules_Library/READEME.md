# 📚 Python Built-in Modules

Python has a **Standard Library** which means it comes with many useful tools pre-installed. You don't need to install anything!

---

## 📂 1. `os` – Operating System

Helps you interact with your computer's folders and files.

```python
import os

# Get current folder path
print(os.getcwd())

# List all files in the current folder
print(os.listdir("."))

# Create a new folder
os.mkdir("new_folder")

# Remove a folder
os.rmdir("new_folder")

# Check if a file exists
print(os.path.exists("main.py"))

# Run a system command (like in your terminal)
os.system("echo Hello World")

# Walk through all directories and files (Deep search)
for root, dirs, files in os.walk("."):
    print("Folder:", root)
    print("Files:", files)
```

---

## ⚙️ 2. `sys` – System Info

Gives information about the Python system and your computer environment.

```python
import sys

# Get arguments passed to the script
print(sys.argv)

# Check Python version
print(sys.version)

# Exit the program immediately
# sys.exit("Stopping program...")

# Get the path where Python looks for modules
# print(sys.path)
```

---

## 🕒 3. `datetime` – Date & Time

Helps you work with dates and times.

```python
from datetime import datetime, date, timedelta

# Get current date and time
now = datetime.now()
print(now)

# Get only today's date
today = date.today()
print(today)

# Format date nicely (Year-Month-Day Hour:Minute)
print(now.strftime("%Y-%m-%d %H:%M"))

# Calculate future or past dates (e.g., +1 day)
tomorrow = now + timedelta(days=1)
print(tomorrow)
```

---

## ⏳ 4. `time` – Time Functions

Simple functions to handle time and delays.

```python
import time

# Pause the program for 2 seconds
print("Waiting...")
time.sleep(2)
print("Done!")

# Get current time as a timestamp number
print(time.time())
```

---

## 🎲 5. `random` – Random Numbers

Generate random numbers or make random choices.

```python
import random

# Random integer between 1 and 100
print(random.randint(1, 100))

# Random decimal number between 0 and 1
print(random.random())

# Pick one random item from a list
print(random.choice(["apple", "banana", "cherry"]))

# Pick multiple random items (allows duplicates)
print(random.choices([1, 2, 3], k=2))

# Pick multiple unique items (no duplicates)
print(random.sample([1, 2, 3, 4], k=2))

# Randomly shuffle a list
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)

# Random decimal in a range (e.g. 1.5 to 10.0)
print(random.uniform(1, 10))
```

---

## ➗ 6. `math` – Mathematics

Advanced math functions like square roots, trigonometry, etc.

```python
import math

# Value of Pi (3.14159...)
print(math.pi)

# Square root
print(math.sqrt(16)) # Output: 4.0

# Round up (Ceiling)
print(math.ceil(4.1)) # Output: 5

# Round down (Floor)
print(math.floor(4.9)) # Output: 4

# Factorial (5! = 5*4*3*2*1)
print(math.factorial(5)) # Output: 120
```

---

## 📝 7. `json` – Data Format

Convert Python dictionaries to JSON text and back. Very useful for saving data or web APIs.

```python
import json

data = {"name": "Alex", "age": 25, "city": "London"}

# Python Dictionary -> JSON String
json_string = json.dumps(data)
print(json_string)

# JSON String -> Python Dictionary
data_back = json.loads(json_string)
print(data_back["name"])
```

---

## 📦 8. `collections` – Advanced Containers

Better ways to store data than just basic lists or dicts.

```python
from collections import Counter, defaultdict, namedtuple

# Counter: Counts elements automatically
words = ["apple", "banana", "apple", "orange"]
count = Counter(words)
print(count) # Output: Counter({'apple': 2, 'banana': 1, 'orange': 1})
print(count.most_common(1)) # Get the most common item

# defaultdict: Dictionary with a default value (no errors for missing keys)
d = defaultdict(int)
d["a"] += 1
print(d["b"]) # Output: 0 (instead of Error)

# namedtuple: Create simple objects to hold data
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)
```

---

## 📁 9. `pathlib` – Modern File Paths

A newer, easier way to handle file paths than `os`.

```python
from pathlib import Path

# Create a path object
path = Path("folder/data.txt")

# Check if file exists
# print(path.exists())

# Get file name and parent folder
print(path.name)   # data.txt
print(path.parent) # folder
```

---

## 🔄 10. `itertools` – Efficient Looping

Tools for advanced loops and iteration.

```python
import itertools

# Combinations: All possible groups of 2
items = ["A", "B", "C"]
for combo in itertools.combinations(items, 2):
    print(combo) # ('A', 'B'), ('A', 'C'), ('B', 'C')

# Count infinitely (starting from 10)
counter = itertools.count(start=10)
print(next(counter)) # 10
print(next(counter)) # 11
```

---

Last Updated\_\_Dec 2025
