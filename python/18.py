def first_even():
    range_size = 10
    if not isinstance(range_size, int) or range_size <= 0:
        print("Invalid range size")
        return
    for i in range(1, range_size):
        if i % 2 == 0:
            print(f"First even: {i}")
            break

first_even()
