def store_coordinates(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Invalid coordinates")
        return
    coords = (x, y)
    print(f"Coordinates: X={coords[0]}, Y={coords[1]}")

store_coordinates(34.05, -118.25)
