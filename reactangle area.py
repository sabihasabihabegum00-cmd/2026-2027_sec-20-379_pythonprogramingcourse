def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

length = float(input("Enter the rectangle's length: "))
width = float(input("Enter the rectangle's width: "))

print("Area:", rectangle_area(length, width))
print("Perimeter:", rectangle_perimeter(length, width))