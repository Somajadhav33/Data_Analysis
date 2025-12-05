# Tuples in Python 

## Tuples in Python (`tuple`)

**Tuples** are Python's **immutable**, **ordered**, and **lightweight** sequences.

### Key Features of Tuples

| Feature                | Tuple                          | List                           |
|------------------------|--------------------------------|--------------------------------|
| Mutable?               | No (Immutable)                 | Yes (Mutable)                  |
| Syntax                 | `(1, 2, 3)` or `1, 2, 3`       | `[1, 2, 3]`                    |
| Performance            | Faster than lists              | Slower                         |
| Memory Usage           | Less memory                    | More memory                    |
| Use Case               | Fixed data, keys in dict, return multiple values | Dynamic/changing data          |
| Allows Duplicates?     | Yes                            | Yes                            |

### Creating Tuples

```python
# Common ways
coordinates = (10, 20)
colors = ("red", "green", "blue")
single = (5,)                    # Note the comma! (important)
empty = ()
also_tuple = 1, 2, 3             # Parentheses optional
mixed = (1, "hello", True, 3.14)

# From list
my_tuple = tuple([1, 2, 3])
```

### All Tuple Operations & Methods

| Operation / Method           | Description                                      | Example                                      |
|------------------------------|--------------------------------------------------|----------------------------------------------|
| **Access**                   | Indexing & slicing (same as list)                | `colors[0]` → `"red"`                        |
|                              | Negative indexing                                | `colors[-1]` → `"blue"`                      |
|                              | Slicing                                          | `colors[1:3]` → `("green", "blue")`          |
| **Length**                   | `len(tuple)`                                     | `len(coordinates)` → `2`                     |
| **Check Membership**         | `in` / `not in`                                  | `"red" in colors` → `True`                   |
| **Concatenation**            | `+` operator                                     | `(1,2) + (3,4)` → `(1,2,3,4)`                |
| **Repetition**               | `*` operator                                     | `("hi",) * 3` → `("hi", "hi", "hi")`         |
| **Count**                    | `.count(item)`                                   | `(1,2,2,3).count(2)` → `2`                   |
| **Index**                    | `.index(item)`                                   | `(10,20,30).index(20)` → `1`                 |

**Note**: Tuples have only **2 methods** — because they are immutable!

### Practical Examples

```python
# Tuple unpacking (Most Pythonic feature!)
point = (5, 10)
x, y = point
print(x, y)        # 5 10

# Swap variables (classic Python trick)
a = 10
b = 20
a, b = b, a        # Now a=20, b=10

# Return multiple values from function
def get_user():
    return ("Shery", 21, "India")

name, age, country = get_user()
print(name, age, country)

# Use as dictionary keys (because immutable!)
locations = {
    (10, 20): "Home",
    (30, 40): "Office"
}
print(locations[(10, 20)])  # "Home"

# Count & Index
data = (1, 2, 2, 3, 2, 4)
print(data.count(2))   # 3
print(data.index(3))   # 3
```

---