def calculate_rectangle_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)) or length < 0 or width < 0:
        print("Invalid inputs")
        return None
    return length * width

area = calculate_rectangle_area(5, 3)
if area is not None:
    print(f"Area: {area}")
