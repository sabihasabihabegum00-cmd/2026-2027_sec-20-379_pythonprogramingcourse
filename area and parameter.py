def rectangle_area_perimeter(l,b): #length,breadth
    area=l*b
    perimeter=2*(l+b)
    return area,perimeter

length =120 # e.g. 5
breath=10 # e.g. 3
area,perimeter =rectangle_area_perimeter(length,breath)
print("Area:", area)
print("perimeter:",perimeter)

