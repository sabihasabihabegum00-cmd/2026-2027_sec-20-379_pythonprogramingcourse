a = float(input("Enter the first angle: "))
b = float(input("Enter the second angle: "))
c = float(input("Enter the third angle: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.")