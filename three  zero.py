matrix = [
    [1, 0, 2],
    [0, 0, 0],
    [4, 0, 5]
]

for row in matrix:
    if row == [0, 0, 0]:
        print("Found a row with three zeros:", row)

for column in range(3):
    if all(matrix[row][column] == 0 for row in range(3)):
        print("Found a column with three zeros.")