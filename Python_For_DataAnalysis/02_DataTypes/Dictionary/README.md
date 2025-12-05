## Dictionaries in Python (`dict`)

**Dictionaries** are Python’s most powerful and widely used data structure.  
They store **key-value pairs** — like a real dictionary: word → meaning.

### Key Features of Dictionaries

| Feature                  | Dictionary (`dict`)           | List/Tuple/Set                     |
|--------------------------|-------------------------------|------------------------------------|
| Mutable?                 | Yes                           | List/Set: Yes / Tuple: No          |
| Ordered?                 | Yes (insertion order ≥ Python 3.7) | List/Tuple: Yes / Set: No         |
| Indexed by               | Keys (any immutable type)     | Integer index                      |
| Duplicates               | Keys: No / Values: Yes        | List/Tuple: Yes / Set: No          |
| Speed                    | Very fast lookup (O(1))       | List/Tuple: O(n) for search        |
| Best For                 | Mapping, configs, JSON, APIs  | Ordered data, unique items         |

### Creating Dictionaries

```python
# Common ways
person = {"name": "Soma", "age": 21, "city": "Sangli"}

# Using dict() constructor
student = dict(name="Alex", age=20, course="Python")

# Empty dict
empty = {}
also_empty = dict()

# With different key types (keys must be immutable!)
mixed_keys = {
    "string": "hello",
    42: "answer",
    (1, 2): "tuple key",
    frozenset({1,2}): "frozenset key"
}
```

### All Dictionary Operations & Methods

| Category                | Operation / Method               | Description                                      | Example                                      |
|-------------------------|----------------------------------|--------------------------------------------------|----------------------------------------------|
| **Access**              | `dict[key]`                      | Get value by key                                 | `person["name"]` → `"Shery"`                 |
|                         | `.get(key, default)`             | Safe access (returns default if missing)         | `person.get("email", "N/A")`                 |
| **Modify / Add**        | `dict[key] = value`              | Add or update                                    | `person["age"] = 22`                         |
|                         | `.update(other_dict)`            | Merge another dict                               | `person.update({"job": "Developer"})`        |
| **Remove**              | `del dict[key]`                  | Delete key                                       | `del person["city"]`                         |
|                         | `.pop(key, default)`             | Remove and return value                          | `age = person.pop("age")`                    |
|                         | `.popitem()`                     | Remove and return last inserted item             | `key, value = person.popitem()`              |
|                         | `.clear()`                       | Remove all items                                 | `person.clear()` → `{}`                      |
| **Check**               | `key in dict`                    | Check if key exists                              | `"name" in person` → `True`                  |
|                         | `.keys()`                        | Get all keys                                     | `person.keys()`                              |
|                         | `.values()`                      | Get all values                                   | `person.values()`                            |
|                         | `.items()`                       | Get all key-value pairs                          | `person.items()`                             |
| **Length**              | `len(dict)`                      | Number of items                                  | `len(person)` → `3`                          |
| **Copy**                | `.copy()`                        | Shallow copy                                     | `new = person.copy()`                        |

### Practical Real-World Examples

```python
# User profile
user = {
    "id": 101,
    "username": "soma",
    "is_active": True,
    "roles": ["student", "mentor"],
    "stats": {"posts": 50, "likes": 1200}
}

# Safe access
email = user.get("email", "No email provided")

# Update nested dict
user["stats"]["likes"] += 100

# Loop through dictionary
for key, value in user.items():
    print(f"{key}: {value}")

# Count word frequency (classic use case!)
text = "python is great and python is fun"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
# → {'python': 2, 'is': 2, 'great': 1, ...}

# Merge two configs
defaults = {"theme": "dark", "font_size": 14}
user_prefs = {"font_size": 16, "notifications": False}
config = {**defaults, **user_prefs}  # Modern way
# Or: config = defaults | user_prefs (Python 3.9+)
```

### Dictionary Comprehensions (Pythonic!)

```python
# Square numbers
squares = {x: x**2 for x in range(6)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter dict
scores = {"Alice": 85, "Bob": 42, "Charlie": 90}
passed = {name: score for name, score in scores.items() if score >= 60}
# → {'Alice': 85, 'Charlie': 90}
```

### Pro Tips & Best Practices

| Tip                                      | Why It Matters                                |
|------------------------------------------|-----------------------------------------------|
| Use `.get()` instead of direct access    | Prevents KeyError                             |
| Use `dict.items()` when looping          | Most efficient and clean                      |
| Use `|` operator for merging (Python 3.9+) | Clean and fast                               |
| Keys must be immutable                   | Strings, numbers, tuples, frozenset only      |
| Dictionaries are ordered since 3.7       | You can rely on insertion order now!          |
---
