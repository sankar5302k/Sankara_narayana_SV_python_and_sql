def countdown():
    count = 5
    if not isinstance(count, int) or count <= 0:
        print("Invalid count")
        return
    while count > 0:
        print(count)
        count -= 1

countdown()
