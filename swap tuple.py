a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

print("Before swapping: a =", a, "b =", b)

# Swap values using tuple unpacking
a, b = b, a

print("After swapping:  a =", a, "b =", b)