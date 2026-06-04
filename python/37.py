class Employee:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Employee Name: {self.name}")

emp1 = Employee("vikram")
emp2 = Employee("navin")
emp1.display_info()
emp2.display_info()
