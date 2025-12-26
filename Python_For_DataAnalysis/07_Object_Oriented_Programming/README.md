# 🐍 Object-Oriented Programming (OOP)

---

## 📑 Table of Contents

1. [🌟 What is OOP?](#-what-is-oop)
2. [🥊 Procedural vs OOP](#-procedural-vs-oop)
3. [🏗️ Classes & Objects](#-classes--objects)
4. [💎 The 4 Pillars of OOP](#-the-4-pillars-of-oop)
   - [Encapsulation (Hiding Data)](#1-encapsulation--hiding-data)
   - [Inheritance (Sharing Features)](#2-inheritance--sharing-features)
   - [Polymorphism (Many Forms)](#3-polymorphism--many-forms)
   - [Abstraction (Hiding Details)](#4-abstraction--hiding-details)
5. [📊 Types of Variables & Methods](#-types-of-variables--methods)
6. [🔮 Magic Methods (Dunder)](#-magic-methods-dunder)
7. [🎨 Decorators (@property, etc.)](#-decorators)
8. [🧬 Advanced Concepts (super, MRO)](#-advanced-concepts)
9. [🧩 Composition vs Inheritance](#-composition-vs-inheritance)
10. [🏦 Simple Project: Student System](#-simple-project-student-system)

---

## 🌟 What is OOP?

**OOP** is just a way to group your code around "things" (Objects) instead of just writing a long list of steps.

Think of it like this:

- **Class**: A recipe for a cake (The Plan).
- **Object**: The actual cake you baked (The Real Thing).
- **Attributes**: The cake's flavor or weight (Data).
- **Methods**: Cutting the cake or eating it (Actions).

---

## 🥊 Procedural vs OOP

| Feature      | Old Way (Procedural)       | New Way (OOP)             |
| :----------- | :------------------------- | :------------------------ |
| **Logic**    | Step-by-step (Top to down) | Based on Objects          |
| **Focus**    | Focus on actions/functions | Focus on data and items   |
| **Security** | Hard to hide data          | Easy to hide/protect data |
| **Reuse**    | Hard to reuse code         | Very easy to reuse code   |

---

## 🏗️ Classes & Objects

A **Class** is like a factory. An **Object** is a product made by that factory.

```python
class Smartphone:
    def __init__(self, brand, model, price):
        # Data for the object
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        # Action the object can do
        print(f"This is a {self.brand} {self.model} costing ${self.price}")

# Creating Objects (Instances)
iphone = Smartphone("Apple", "iPhone 15", 999)
samsung = Smartphone("Samsung", "S23", 899)

iphone.show_info()   # Output: This is a Apple iPhone 15 costing $999
samsung.show_info()  # Output: This is a Samsung S23 costing $899
```

---

## 💎 The 4 Pillars of OOP

### 1. Encapsulation – Hiding Data

This is like a capsule. It keeps the data safe inside. We use `__` (double underscore) to make things "Private" so they cannot be changed easily from outside.

```python
class Bank:
    def __init__(self, money):
        self.__balance = money # Private (Hidden)

    def show_balance(self):
        print(f"Your balance is: ${self.__balance}")

my_bank = Bank(1000)
my_bank.show_balance()
# print(my_bank.__balance) # ❌ This will give an error!
```

### 2. Inheritance – Sharing Features

A "Child" class can copy everything from a "Parent" class. This saves time!

```python
class Animal: # Parent
    def eat(self):
        print("Eating food...")

class Dog(Animal): # Child (takes everything from Animal)
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog()
my_dog.eat()  # Found in Parent
my_dog.bark() # Found in Child
```

### 3. Polymorphism – Many Forms

The same name can do different things. Like the word "Run". A person runs, a car runs, and a computer runs—but they all do it differently.

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# Same method name, different results
for pet in [Cat(), Dog()]:
    pet.sound()
```

### 4. Abstraction – Hiding Details

Abstraction means showing only the important parts and hiding the complex background work. You don't need to know how an engine works to drive a car.

_Note: We don't need any special module for this, just simple logic!_

```python
class Laptop:
    def start(self):
        self.__boot_bios()
        self.__load_os()
        print("Laptop is ready!")

    def __boot_bios(self): # Hidden detail
        print("Checking hardware...")

    def __load_os(self): # Hidden detail
        print("Loading Windows...")

dell = Laptop()
dell.start() # You only call 'start', the rest is hidden!
```

---

## 📊 Types of Variables & Methods

### Variables

1. **Instance Variable**: Unique to each object (e.g., `self.name`).
2. **Class Variable**: Same for everyone in the class (e.g., `school_name`).

### Methods

1. **Instance Method**: Uses `self`. Normal actions.
2. **Class Method**: Uses `@classmethod`. Used for things related to the whole class.
3. **Static Method**: Uses `@staticmethod`. Just a regular function that lives inside a class.

---

## 🔮 Magic Methods (Dunder)

These special methods start and end with `__`. They let you do cool things with symbols like `+` or `print`.

- `__init__`: Runs automatically when you create an object.
- `__str__`: Tells Python what to show when you `print(object)`.

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Name: {self.title}"

my_book = Book("Python Basics")
print(my_book) # Output: Book Name: Python Basics
```

---

## 🎨 Decorators

- **@property**: Lets you use a method like a simple variable (you don't need to call it with `()`).

```python
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

p = Person("John", "Doe")
print(p.full_name) # No brackets needed!
```

---

## 🧬 Advanced Concepts

### `super()`

Used to call the Parent's code from the Child.

```python
class Mom:
    def hobby(self):
        print("Cooking")

class Son(Mom):
    def hobby(self):
        super().hobby() # Calls Mom's hobby
        print("Coding")

me = Son()
me.hobby() # Prints Cooking then Coding
```

### MRO (Order)

Python follows an order to find which method to use if there are many parents.

---

## 🧩 Composition vs Inheritance

- **Inheritance (IS-A)**: A Dog _is an_ Animal.
- **Composition (HAS-A)**: A Car _has an_ Engine.

Composition is when one class uses an object of another class.

---

## 🏦 Simple Project: Student System

```python
class Student:
    school = "City School" # Class Variable

    def __init__(self, name, marks):
        self.name = name     # Instance Variable
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Rahul", 85)
print(f"{s1.name} from {s1.school} is {s1.result()}")
```

---
