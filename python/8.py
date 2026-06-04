def find_min_max(salaries):
    if not isinstance(salaries, list) or not salaries:
        print("Invalid input")
        return
    highest = max(salaries)
    lowest = min(salaries)
    print(f"Highest Salary: {highest}")
    print(f"Lowest Salary: {lowest}")

salaries = [50000, 75000, 62000, 95000]
find_min_max(salaries)
