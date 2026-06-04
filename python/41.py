import json
import os

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}"

emps = {"1": Employee("1", "vikram"), "2": Employee("2", "navin")}
data = {k: v.name for k, v in emps.items()}
with open("emps.json", 'w') as f:
    json.dump(data, f)

loaded = {}
if os.path.exists("emps.json"):
    with open("emps.json", 'r') as f:
        data = json.load(f)
    loaded = {k: Employee(k, v) for k, v in data.items()}

for emp in loaded.values():
    print(emp)
