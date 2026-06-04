def kg_to_lbs():
    kg_str = input("Enter weight in kg: ").strip()
    try:
        kg = float(kg_str)
    except ValueError:
        print("Invalid input")
        return
    lbs = kg * 2.20462
    print(f"Weight in pounds: {lbs:.2f}")

kg_to_lbs()
