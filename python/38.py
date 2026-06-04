class Employee:
    def __init__(self, salary):
        self.salary = salary

    def set_salary(self, amount):
        if amount > 0:
            self.salary = amount
        return self

    def apply_raise(self, percent):
        if percent > 0:
            self.salary += self.salary * (percent / 100)
        return self

    def display(self):
        print(f"Final Salary: {self.salary:.2f}")
        return self

emp = Employee(50000)
emp.set_salary(60000).apply_raise(10).display()
