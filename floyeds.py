rows = int(input("Enter the number of rows: "))

number = 1

for row in range(1, rows + 1):
    for column in range(row):
        print(number, end=" ")
        number += 1
    print()