# calculator
A multi-language calculator project that uses Python for addition, C for subtraction, JavaScript for division, and Lua for multiplication, showcasing cross-language integration.

# Multi-Language Calculator

A **multi-language calculator** project demonstrating the integration of Python, C, JavaScript, and Lua. Each language handles a specific mathematical operation:

- **Python**: Addition
- **C**: Subtraction
- **JavaScript**: Division
- **Lua**: Multiplication

---

## Features

- Demonstrates cross-language integration.
- Modular design, with each operation implemented in a separate language.
- A Python script (`main.py`) orchestrates the entire process.

---

## Prerequisites

Ensure you have the following installed on your system:

1. **Python** (>= 3.6)
2. **GCC** (for compiling C code)
3. **Node.js** (for running JavaScript code)
4. **Lua** and **lupa** (Python library for Lua integration)

To install `lupa`, run:
```bash
pip install lupa


### Compile the C Code

Use GCC to compile the subtraction logic into a shared library:

```bash
gcc -shared -o subtraction.so -fPIC subtraction.c
