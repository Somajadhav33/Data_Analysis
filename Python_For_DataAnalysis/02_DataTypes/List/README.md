
## Lists in Python (`list`)
**Lists** are one of the most powerful and commonly used data types in Python.

### What is a List?

- **Ordered** → Items have a defined sequence
- **Mutable** → You can change, add, remove items after creation
- **Allows duplicates**
- **Can hold any data type** (mixed types allowed)

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14, None]
empty = []
```

### Creating Lists

```python
# Common ways
lst1 = [1, 2, 3]
lst2 = list((1, 2, 3))        # Using list() constructor
lst3 = [x for x in range(5)]  # List comprehension
zeros = [0] * 10              # [0, 0, 0, ..., 0]
```

### All List Operations & Methods

| Category               | Operation / Method                | Description                                      | Example                                      |
|------------------------|-----------------------------------|--------------------------------------------------|----------------------------------------------|
| **Access**             | Indexing                          | Get item by index                                | `fruits[0]` → `"apple"`                      |
|                        | Negative Indexing                 | Access from end                                  | `fruits[-1]` → `"cherry"`                    |
|                        | Slicing                           | Get sublist                                      | `fruits[1:3]` → `["banana", "cherry"]`       |
| **Modify**             | `lst[index] = value`              | Change item                                      | `fruits[0] = "orange"`                       |
| **Add Items**          | `.append(item)`                   | Add to end                                       | `fruits.append("grape")`                     |
|                        | `.extend(iterable)`               | Add multiple items                               | `fruits.extend(["kiwi", "mango"])`           |
|                        | `.insert(index, item)`            | Insert at specific position                      | `fruits.insert(1, "lemon")`                  |
|                        | `+` operator                      | Concatenate lists                                | `[1,2] + [3,4]` → `[1,2,3,4]`                |
| **Remove Items**       | `.remove(item)`                   | Remove first occurrence                          | `fruits.remove("banana")`                    |
|                        | `.pop(index)`                     | Remove and return item (default: last)           | `fruits.pop()` → returns last item           |
|                        | `.clear()`                        | Remove all items                                 | `fruits.clear()` → `[]`                      |
|                        | `del lst[index]`                  | Delete by index                                  | `del fruits[0]`                              |
|                        | `del lst`                         | Delete entire list                               | `del fruits`                                 |
| **Search**             | `.index(item)`                    | Find first index of item                         | `fruits.index("cherry")` → `2`               |
|                        | `.count(item)`                    | Count occurrences                                | `[1,1,2].count(1)` → `2`                     |
|                        | `in` operator                     | Check if item exists                             | `"apple" in fruits` → `True`                 |
| **Sorting**            | `.sort()`                         | Sort list in-place (ascending)                   | `numbers.sort()`                             |
|                        | `.sort(reverse=True)`             | Sort descending                                  | `numbers.sort(reverse=True)`                 |
|                        | `.reverse()`                      | Reverse the list                                 | `fruits.reverse()`                           |
|                        | `sorted(lst)`                     | Return new sorted list (doesn't modify original) | `sorted(numbers)`                            |
| **Copy**               | `.copy()`                         | Shallow copy                                     | `new = fruits.copy()`                        |
|                        | `list(lst)`                       | Another way to copy                              | `new = list(fruits)`                         |
| **Length**             | `len(lst)`                        | Number of items                                  | `len(fruits)` → `3`                          |

### Practical Examples

```python
# Create list
cars = ["BMW", "Tesla", "Audi", "Ford"]

# Access
print(cars[1])        # Tesla
print(cars[-1])       # Ford

# Modify
cars[1] = "Mercedes"

# Add items
cars.append("Honda")
cars.insert(0, "Lamborghini")
cars.extend(["Toyota", "Suzuki"])

# Remove items
cars.remove("Ford")
last = cars.pop()     # Removes and returns last item
cars.clear()          # Empty list

# Useful operations
numbers = [5, 2, 8, 1, 9]
numbers.sort()                    # [1, 2, 5, 8, 9]
numbers.reverse()                 # [9, 8, 5, 2, 1]
print(numbers.count(5))           # 1
print(8 in numbers)               # True

# List comprehension (Pythonic way)
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, ...]
evens = [x for x in range(20) if x % 2 == 0]
```

### Quick Cheat Sheet

```python
lst = [10, 20, 30, 40]

lst.append(50)          # [10,20,30,40,50]
lst.insert(0, 5)        # [5,10,20,30,40,50]
lst.pop()               # 50
lst.remove(20)          # [5,10,30,40]
lst.index(30)           # 2
len(lst)                # 4
lst.reverse()           # [40,30,10,5]
lst.sort()              # [5,10,30,40]
```
