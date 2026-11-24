rows = int(input("Enter the number of rows for the top half: "))

# Top half, including the middle row
for row in range(1, rows + 1):
    spaces = rows - row
    if row == 1:
        print(" " * spaces + "*")
    else:
        inside_spaces = 2 * row - 3
        print(" " * spaces + "*" + " " * inside_spaces + "*")

# Bottom half
for row in range(rows - 1, 0, -1):
    spaces = rows - row
    if row == 1:
        print(" " * spaces + "*")
    else:
        inside_spaces = 2 * row - 3
        print(" " * spaces + "*" + " " * inside_spaces + "*")