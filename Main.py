import math

try:
    n = float(input("Enter a non‑negative number: "))
    if n < 0:
        raise ValueError("Negative value")
    print(f"√{n} = {math.sqrt(n)}")
except ValueError:
    print("Please enter a valid non‑negative number.")