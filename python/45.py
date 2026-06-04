import csv
import os
from datetime import datetime
from collections import defaultdict

filename = "expenses.csv"
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Amount", "Category"])
        writer.writerow(["2023-10-01", "50", "Food"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), "100", "Transport"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), "200", "Food"])

current_month = datetime.now().month
current_year = datetime.now().year
summary = defaultdict(float)

with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            date_obj = datetime.strptime(row["Date"], "%Y-%m-%d")
            if date_obj.month == current_month and date_obj.year == current_year:
                summary[row["Category"]] += float(row["Amount"])
        except ValueError:
            continue

for category, total in summary.items():
    print(f"Category: {category}, Total: {total:.2f}")
