def sum_odd_numbers():
    range_size = 10
    if not isinstance(range_size, int) or range_size <= 0:
        print("Invalid range size")
        return
    total = 0
    for i in range(range_size):
        if i % 2 == 0:
            continue
        total += i
    print(f"Sum of odd numbers: {total}")

sum_odd_numbers()
