from math import *

def demonstrate_math():
    num = 16
    if not isinstance(num, (int, float)) or num < 0:
        print("Invalid input")
        return
    print(f"Square root of {num}: {sqrt(num)}")
    print(f"2 to the power of 3: {pow(2, 3)}")
    print(f"Value of Pi: {pi}")

demonstrate_math()
