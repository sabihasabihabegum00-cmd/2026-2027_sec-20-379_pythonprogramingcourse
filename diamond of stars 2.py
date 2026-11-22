# Print a diamond pattern of stars

rows = int(input("Enter the number of rows for the top half: "))

# Top half, including the middle row
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Bottom half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)