rows = int(input("Enter the number of rows for the top half: "))

# Top half, including the middle row
for row in range(1, rows + 1):
    spaces = rows - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)

# Bottom half
for row in range(rows - 1, 0, -1):
    spaces = rows - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)