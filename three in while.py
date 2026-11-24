# Print numbers 1 to 9 in a 3 × 3 grid
# The outer loop uses while; the inner loop uses for.

number = 1
row = 0

while row < 3:
    for column in range(3):
        print(number, end=" ")
        number += 1
    print()
    row += 1