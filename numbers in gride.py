# Print numbers in a 3 × 3 grid

number = 1

for row in range(3):
    for column in range(3):
        print(number, end=" ")
        number += 1
    print()