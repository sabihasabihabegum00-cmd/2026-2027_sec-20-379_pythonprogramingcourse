# Create two 2 × 2 matrices
matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

# Add the matrices
addition = [
    [matrix_a[row][col] + matrix_b[row][col] for col in range(2)]
    for row in range(2)
]

# Multiply the matrices
multiplication = [
    [
        sum(matrix_a[row][k] * matrix_b[k][col] for k in range(2))
        for col in range(2)
    ]
    for row in range(2)
]

print("Addition:")
for row in addition:
    print(row)

print("Multiplication:")
for row in multiplication:
    print(row)