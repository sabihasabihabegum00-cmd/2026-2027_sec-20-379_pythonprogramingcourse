rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()