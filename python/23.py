import math

def calculate_area(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        print("Invalid radius")
        return
    area = math.pi * (radius ** 2)
    print(f"Area: {area:.2f}")

calculate_area(5)
