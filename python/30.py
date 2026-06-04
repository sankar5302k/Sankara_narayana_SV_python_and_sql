def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Inputs must be numbers")

divide_numbers(10, 0)
