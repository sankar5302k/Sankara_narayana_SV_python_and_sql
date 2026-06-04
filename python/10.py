def next_year_age():
    age_str = input("Enter your age: ").strip()
    if not age_str.isdigit():
        print("Invalid input")
        return
    age = int(age_str)
    print(f"Next year you'll be {age + 1}")

next_year_age()
