def merge_employees(emp_dict1, emp_dict2):
    if not isinstance(emp_dict1, dict) or not isinstance(emp_dict2, dict):
        print("Inputs must be dictionaries")
        return
    emp_dict1.update(emp_dict2)
    print(f"Updated Employee Data: {emp_dict1}")

dict1 = {"vikram": "HR", "navin": "Engineering"}
dict2 = {"srikanth": "Marketing", "navin": "Sales"}
merge_employees(dict1, dict2)
