# Create a 3 × 3 grid filled with zeros
grid = []

for row in range(3):
    grid.append([0, 0, 0])

# Display the grid
for row in grid:
    print(*row)