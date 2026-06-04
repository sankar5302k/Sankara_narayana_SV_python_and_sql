def print_numbers():
    count = 5
    if not isinstance(count, int) or count < 0:
        print("Invalid count")
        return
    for i in range(1, count + 1):
        print(i)

print_numbers()
