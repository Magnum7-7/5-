def add(a, b):
    return a + b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

if __name__ == "__main__":
    print("Calculator v1.2.0")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
  
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print("Calculator (Division Feature Branch)")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"6 / 2 = {divide(6, 2)}")
