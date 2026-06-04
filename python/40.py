class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        parts = emp_str.split(',')
        if len(parts) != 2:
            raise ValueError("Invalid format")
        name = parts[0]
        salary = int(parts[1])
        return cls(name, salary)

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

emp = Employee.from_string("vikram,75000")
emp.display()
