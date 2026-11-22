# Matrix operations using nested lists
# This program adds, subtracts, and multiplies two matrices.

def read_matrix(rows, columns, name):
    matrix = []
    print(f"Enter the values for matrix {name}, one row at a time:")

    for i in range(rows):
        while True:
            values = input(f"Row {i + 1}: ").split()
            if len(values) == columns:
                matrix.append([float(value) for value in values])
                break
            print(f"Please enter exactly {columns} numbers.")

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:g}" for value in row))


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix_a = read_matrix(rows, columns, "A")
matrix_b = read_matrix(rows, columns, "B")

print("\nMatrix A:")
print_matrix(matrix_a)

print("\nMatrix B:")
print_matrix(matrix_b)

# Addition and subtraction require matrices of the same size.
addition = [
    [matrix_a[i][j] + matrix_b[i][j] for j in range(columns)]
    for i in range(rows)
]
subtraction = [
    [matrix_a[i][j] - matrix_b[i][j] for j in range(columns)]
    for i in range(rows)
]

print("\nA + B:")
print_matrix(addition)

print("\nA - B:")
print_matrix(subtraction)

# Multiplication is possible here because both matrices are rows × columns.
# It requires columns == rows.
if columns == rows:
    multiplication = [
        [
            sum(matrix_a[i][k] * matrix_b[k][j] for k in range(columns))
            for j in range(columns)
        ]
        for i in range(rows)
    ]

    print("\nA × B:")
    print_matrix(multiplication)
else:
    print("\nA × B is not possible: for these square matrices, rows and columns must match.")