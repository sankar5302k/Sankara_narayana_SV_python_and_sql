def get_employee_salary(dept_data, dept_name, emp_name):
    if not isinstance(dept_data, dict):
        print("Invalid department data")
        return
    dept = dept_data.get(dept_name)
    if not dept:
        print("Department not found")
        return
    salary = dept.get(emp_name)
    if not salary:
        print("Employee not found in department")
        return
    print(f"Salary of {emp_name}: {salary}")

data = {
    "Engineering": {"vikram": 80000, "navin": 90000},
    "HR": {"srikanth": 60000}
}
get_employee_salary(data, "Engineering", "vikram")
