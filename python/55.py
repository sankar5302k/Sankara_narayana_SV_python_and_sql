import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount
        if self.spent > self.limit:
            print(f"ALERT: Overspending in {self.name}!")

budget = {
    "Food": Category("Food", 300),
    "Rent": Category("Rent", 1000),
    "Utilities": Category("Utilities", 200),
    "Entertainment": Category("Entertainment", 150)
}


while True:
    category = input("Enter category (Food, Rent, Utilities, Entertainment) or 'exit': ")
    if category == "exit":
        break
    if category in budget:
        amount = float(input("Enter spending amount: "))
        budget[category].add_expense(amount)
    else:
        print("Invalid category")

print("Budget Summary:")
for cat in budget.values():
    print(f"{cat.name}: Spent ${cat.spent} / Limit ${cat.limit}")

categories = list(budget.keys())
spent = [cat.spent for cat in budget.values()]

plt.subplot(2,1,1)
plt.pie(spent, labels=categories)
plt.title("Spending Distribution")

plt.subplot(2,1,2)
plt.bar(categories, spent)
plt.title("Spending by Category")

plt.show()
