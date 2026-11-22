# Print an inverted right-angled triangle using stars

rows = int(input("Enter the number of rows: "))

for row in range(rows, 0, -1):
    print("* " * row)