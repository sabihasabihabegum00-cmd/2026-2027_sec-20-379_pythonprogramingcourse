rows = int(input("Enter the number of rows: "))

for row in range(1, rows + 1):
    # Add spaces to center the pyramid
    print(" " * (rows - row), end="")

    # Print numbers from 1 up to the row number
    for number in range(1, row + 1):
        print(number, end=" ")

    print()