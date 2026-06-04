import csv
import os

filename = "employees.csv"
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Salary"])
        writer.writerow(["vikram", "60000"])
        writer.writerow(["navin", "40000"])
        writer.writerow(["srikanth", "70000"])

try:
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        salaries = [int(row["Salary"]) for row in reader if int(row["Salary"]) > 50000]
        if salaries:
            avg = sum(salaries) / len(salaries)
            print(f"Average salary (>50000): {avg:.2f}")
        else:
            print("No employees found with salary > 50000")
except Exception as e:
    print(f"Error: {e}")
