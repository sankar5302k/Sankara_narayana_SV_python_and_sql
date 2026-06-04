def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Invalid inputs")
        return None
    return a + b

print(f"Result: {add(5, 3)}")
