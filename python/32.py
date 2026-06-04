def add_expense(expenses, amount):
    if not isinstance(expenses, list):
        print("Expenses must be a list")
        return
    if not isinstance(amount, (int, float)) or amount < 0:
        print("Invalid expense amount")
        return
    expenses.append(amount)
    print(f"Updated Expenses: {expenses}")

expenses = [50, 20]
add_expense(expenses, 30)
