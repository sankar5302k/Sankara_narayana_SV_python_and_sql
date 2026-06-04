def calculate_total_salary(base, bonus):
    if not isinstance(base, (int, float)) or not isinstance(bonus, (int, float)):
        print("Invalid input")
        return None
    total = base + bonus
    return total

base = 50000
bonus = 5000
total = calculate_total_salary(base, bonus)
print(f"Total Salary: {total}")
