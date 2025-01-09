import ctypes  # To call C functions
import subprocess  # To call JavaScript (Node.js)
import lupa  # To run Lua scripts

# Load the C shared library
c_library = ctypes.CDLL('./subtraction.so')

# Lua runtime
lua_runtime = lupa.LuaRuntime()

# Load the Lua script
with open("multiplication.lua", "r") as lua_file:
    lua_script = lua_file.read()
lua_runtime.execute(lua_script)
lua_multiply = lua_runtime.globals().multiply

def add(a, b):
    return a + b

def subtract(a, b):
    return c_library.subtract(ctypes.c_int(a), ctypes.c_int(b))

def divide(a, b):
    result = subprocess.run(
        ['node', 'division.js', str(a), str(b)],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def multiply(a, b):
    return lua_multiply(a, b)

if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("Addition (Python):", add(a, b))
    print("Subtraction (C):", subtract(a, b))
    print("Division (JavaScript):", divide(a, b))
    print("Multiplication (Lua):", multiply(a, b))

