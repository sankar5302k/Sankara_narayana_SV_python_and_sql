def calculate_net_salary(salary, tax_rate):
    if salary < 0 or tax_rate < 0 or tax_rate > 1:
        print("Invalid input")
        return
    net_salary = salary * (1 - tax_rate)
    print(f"Net Salary: {net_salary:.2f}")

salary = 75000.5
tax_rate = 0.18
calculate_net_salary(salary, tax_rate)
