def split_bill(total_bill, people):
    if not isinstance(total_bill, (int, float)) or not isinstance(people, int) or people <= 0:
        print("Invalid input")
        return
    share = total_bill // people
    print(f"Individual share: {share}")

total_bill = 1250
people = 4
split_bill(total_bill, people)
