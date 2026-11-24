rows = int(input("Enter the number of rows: "))

for row in range(rows):
    # Center each row
    print(" " * (rows - row), end="")

    value = 1
    for column in range(row + 1):
        print(value, end=" ")
        value = value * (row - column) // (column + 1)

    print()