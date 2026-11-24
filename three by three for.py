# Print numbers 1 to 9 in a 3 × 3 grid using nested for loops
number = 1

for row in range(3):
    for column in range(3):
        print(number, end=" ")
        number += 1
    print()