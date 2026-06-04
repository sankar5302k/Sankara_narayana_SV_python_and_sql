def display_coordinates(coords):
    if not isinstance(coords, tuple) or len(coords) != 2:
        print("Invalid coordinates")
        return
    x, y = coords
    print(f"X: {x}, Y: {y}")

coords = (10, 20)
display_coordinates(coords)
