def greet_user():
    name = input("Enter your name: ").strip()
    if not name:
        print("Invalid input: name cannot be empty")
        return
    print(f"Hello, {name}!")

greet_user()
