# Print numbers in a 3 × 3 grid using nested while loops

number = 1
row = 0

while row < 3:
    column = 0

    while column < 3:
        print(number, end=" ")
        number += 1
        column += 1

    print()
    row += 1