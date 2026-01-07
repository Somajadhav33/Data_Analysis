## What is NumPy?

NumPy is the fundamental open-source library for scientific computing in Python. It provides:

- A powerful **N-dimensional array object** (`ndarray`).
- High-performance functions for numerical operations.
- Tools for linear algebra, Fourier transforms, random numbers, and more.

NumPy is fast (implemented in C), memory-efficient, and forms the foundation for libraries like Pandas, SciPy, and scikit-learn.

**Latest version** (as of January 2026): NumPy 2.4.x

### Installation
```bash
pip install numpy
```

## NumPy Arrays vs. Python Lists

NumPy arrays are specialized for numerical data, while Python lists are general-purpose.

| Feature                  | NumPy Array                          | Python List                              |
|--------------------------|--------------------------------------|------------------------------------------|
| Data Types               | Homogeneous (same type)             | Heterogeneous (mixed types)              |
| Performance              | Very fast (vectorized, C-backed)    | Slower for numerical ops                |
| Memory                   | Efficient (contiguous block)        | Higher overhead (pointers)              |
| Operations               | Vectorized (e.g., `arr * 2`)        | Requires loops                          |
| Dimensions               | Native multi-dimensional support    | Simulated with nested lists             |




**Performance Example**:
NumPy can be 20–50x faster for large numerical operations.

## 1D and Multi-Dimensional Arrays in NumPy

NumPy's `ndarray` supports any number of dimensions.

- **1D Array** (vector): Linear sequence.
  ```python
  np.array([1, 2, 3, 4])  # Shape: (4,)
  ```

- **2D Array** (matrix): Rows and columns.
  ```python
  np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
  ```

- **3D Array**: Stack of matrices (e.g., images: height × width × channels).
  ```python
  np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Shape: (2, 2, 2)
  ```








All arrays support broadcasting, slicing, and vectorized operations uniformly.

## What is Jupyter Notebook?

Jupyter Notebook is a web-based interactive environment for creating **notebook documents** (`.ipynb`) that combine:

- Executable code (Python, R, Julia, etc.).
- Rich text (Markdown).
- Equations (LaTeX).
- Visualizations and multimedia.

Perfect for exploratory data analysis, teaching, and reproducible research.








**Modern recommendation**: Use **JupyterLab** (next-gen interface with tabs, file browser, etc.).

### Installation
```bash
pip install notebook  # Classic
pip install jupyterlab  # Recommended
```

Launch with:
```bash
jupyter lab
```