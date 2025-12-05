# Sets in Python (`set`) 

##  Sets in Python (`set` & `frozenset`)

**Sets** are unordered, mutable collections of **unique** items.  
Perfect for removing duplicates, membership testing, and mathematical operations!

### Key Features of Sets

| Feature                | Set (`set`)                  | List/Tuple                  | Dictionary                  |
|------------------------|------------------------------|-----------------------------|-----------------------------|
| Mutable?               | Yes                          | List: Yes / Tuple: No       | Yes (keys/values)           |
| Ordered?               | No (Unordered)               | Yes                         | Yes (insertion order ≥3.7)  |
| Duplicates?            | No (Automatically removed)   | Yes                         | Keys: No / Values: Yes      |
| Indexing/Slicing       | Not allowed                  | Yes                         | Keys only                   |
| Best For               | Unique items, math operations| Ordered data                | Key-value mapping           |

### Creating Sets

```python
# Common ways
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty = set()                        # Note: {} makes dict, not set!
mixed = {1, "hello", True, 3.14}

# Remove duplicates automatically
duplicates = {1, 1, 2, 2, 3, 3}       # → {1, 2, 3}

# From list/tuple/string
unique_chars = set("abracadabra")    # {'a', 'b', 'r', 'c', 'd'}
```

### All Set Operations & Methods

| Category               | Operation / Method           | Description                                   | Example                                      |
|------------------------|------------------------------|-----------------------------------------------|----------------------------------------------|
| **Add Items**          | `.add(item)`                 | Add single item                               | `fruits.add("orange")`                       |
|                        | `.update(iterable)`          | Add multiple items                            | `fruits.update(["mango", "grape"])`          |
| **Remove Items**       | `.remove(item)`              | Remove item (raises KeyError if not found)    | `fruits.remove("banana")`                    |
|                        | `.discard(item)`             | Remove item (no error if not found)           | `fruits.discard("ghost")`                    |
|                        | `.pop()`                     | Remove and return random item                 | `item = fruits.pop()`                        |
|                        | `.clear()`                   | Remove all items                              | `fruits.clear()` → `set()`                   |
| **Membership Test**    | `in` / `not in`              | Very fast (O(1))                              | `"apple" in fruits` → `True`                 |
| **Length**             | `len(set)`                   | Number of items                               | `len(fruits)`                                |
| **Mathematical Ops**   | `|` (union)                  | All items from both sets                      | `a | b`                                      |
|                        | `&` (intersection)           | Common items                                  | `a & b`                                      |
|                        | `-` (difference)             | Items in first but not second                 | `a - b`                                      |
|                        | `^` (symmetric difference)   | Items in either but not both                  | `a ^ b`                                      |
| **In-place Ops**       | `|=`, `&=`, `-=`, `^=`       | Modify set directly                           | `fruits |= {"kiwi"}`                         |
| **Comparison**         | `.issubset()`                | Check if all items are in another set         | `{1,2}.issubset({1,2,3})` → `True`           |
|                        | `.issuperset()`              | Check if contains all items                   | `{1,2,3}.issuperset({1,2})` → `True`         |
|                        | `.isdisjoint()`              | No common items                               | `{1,2}.isdisjoint({3,4})` → `True`           |
| **Copy**               | `.copy()`                    | Shallow copy                                  | `new = fruits.copy()`                        |

### Practical Examples

```python
# Remove duplicates from list (most common use!)
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))        # [1, 2, 3, 4, 5]

# Fast membership testing
allowed = {"admin", "moderator", "user"}
if user_role in allowed:
    print("Access granted!")

# Set operations
online_now = {"Alice", "Bob", "Charlie"}
online_yesterday = {"Bob", "David", "Eve"}

# Who was online both days?
both_days = online_now & online_yesterday           # {"Bob"}

# Who joined today?
new_users = online_now - online_yesterday           # {"Alice", "Charlie"}

# Who was online either day?
all_users = online_now | online_yesterday           # {"Alice", "Bob", "Charlie", "David", "Eve"}

# Who changed (came or left)?
changed = online_now ^ online_yesterday             # {"Alice", "Charlie", "David", "Eve"}
```

### `frozenset` – Immutable Sets

```python
frozen = frozenset([1, 2, 3])
# frozen.add(4)    # Error! Immutable

# Can be used as dictionary keys!
cache = {
    frozenset({1, 2}): "result1",
    frozenset({3, 4}): "result2"
}
```

### Pro Tips

| Tip                                      | Why It Matters                               |
|------------------------------------------|----------------------------------------------|
| Use `set()` to remove duplicates         | Fastest and cleanest way                     |
| Prefer `discard()` over `remove()`       | Avoids errors when item might not exist      |
| Use set operations instead of loops      | Much faster and more readable                |
| Sets are extremely fast for `in` checks  | O(1) vs O(n) for lists                       |
| Use `frozenset` for dict keys or set items | Only immutable types can be hashed         |
---