# Check whether three angles can form a valid triangle

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
    print("These angles form a valid triangle.")
else:
    print("These angles do not form a valid triangle.")