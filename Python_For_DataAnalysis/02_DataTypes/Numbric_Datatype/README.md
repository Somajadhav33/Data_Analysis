
## Numeric Data Types in Python – Complete Reference

Python has three main built-in numeric types:

| Type      | Name            | Mutable? | Examples                          |
|-----------|-----------------|----------|-----------------------------------|
| `int`     | Integer         | No       | `42`, `-10`, `0`, `999999999`     |
| `float`   | Floating Point  | No       | `3.14`, `-0.001`, `2.5e3`         |
| `complex` | Complex Number  | No       | `3+5j`, `-2j`, `1.5+2.7j`         |

### 1. Integer (`int`) – Unlimited Precision!

```python
age = 25
big_num = 999999999999999999999999
negative = -100
```

#### Common int Methods

| Method                    | Description                                | Example                             |
|---------------------------|--------------------------------------------|-------------------------------------|
| `.bit_length()`          | Number of bits needed to represent         | `(5).bit_length()` → `3`            |
| `.to_bytes(length, byteorder)` | Convert to bytes                      | `(10).to_bytes(2, 'big')`           |
| `.from_bytes(bytes, byteorder)` | Create int from bytes                | `int.from_bytes(b'\x00\x0a', 'big')` → `10` |
| `.as_integer_ratio()`     | (For floats, not int)                      | —                                   |
| `bin(x)`                  | Binary string (`0b...`)                    | `bin(10)` → `'0b1010'`              |
| `hex(x)`                  | Hexadecimal (`0x...`)                      | `hex(255)` → `'0xff'`               |
| `oct(x)`                  | Octal (`0o...`)                            | `oct(8)` → `'0o10'`                 |


### 2. Float (`float`) – 

```python
price = 19.99
pi = 3.14159
scientific = 1.5e-7   # 0.00000015
```

#### Important float Methods

| Method                     | Description                                      | Example                                  |
|----------------------------|--------------------------------------------------|------------------------------------------|
| `.as_integer_ratio()`      | Return (numerator, denominator) as fraction      | `(0.25).as_integer_ratio()` → `(1, 4)`   |
| `.hex()`                   | Hex representation of float                      | `(10.5).hex()` → `'0x1.5000000000000p+3'` |
| `.is_integer()`            | Check if float is whole number                   | `(10.0).is_integer()` → `True`           |
| `float.fromhex('hex_str')` | Create float from hex string                     | `float.fromhex('0x1.8p+3')` → `12.0`     |

**Special float values**:
```python
float('inf')    # Infinity
float('-inf')   # Negative infinity
float('nan')    # Not a Number
```

### 3. Complex Numbers (`complex`)

Used in scientific computing, electrical engineering, etc.

```python
z1 = 3 + 4j
z2 = complex(2, -5)
z3 = 1j * 1j   # → (-1+0j) because j² = -1
```

#### Complex Number Attributes & Methods

| Attribute/Method        | Description                          | Example                         |
|-------------------------|--------------------------------------|---------------------------------|
| `.real`                 | Real part                            | `(3+4j).real` → `3.0`           |
| `.imag`                 | Imaginary part                       | `(3+4j).imag` → `4.0`           |
| `.conjugate()`          | Complex conjugate (3+4j → 3-4j)       | `(3+4j).conjugate()` → `(3-4j)` |
| `abs(z)`                | Magnitude / modulus                  | `abs(3+4j)` → `5.0`             |
| `z1 + z2`, `z1 * z2`    | Addition & multiplication            | Supported natively              |

### Built-in Math Functions (Work with int & float)

| Function           | Description                          | Example                     |
|--------------------|--------------------------------------|-----------------------------|
| `abs(x)`           | Absolute value                       | `abs(-5)` → `5`             |
| `round(number, ndigits)` | Round to given digits          | `round(3.14159, 2)` → `3.14`|
| `pow(base, exp)`   | Power (same as `**`)                 | `pow(2, 10)` → `1024`       |
| `divmod(x, y)`     | Quotient and remainder               | `divmod(10, 3)` → `(3, 1)`  |
| `max()`, `min()`   | Maximum/minimum                      | `max(1, 5, 2)` → `5`        |
| `sum(iterable)`    | Sum of numbers                       | `sum([1,2,3,4])` → `10`     |

---