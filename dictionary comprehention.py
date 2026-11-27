# A dictionary comprehension creates a dictionary using a short loop.

numbers = [1, 2, 3, 4, 5]

# Use each number as a key and its square as the value
squares = {number: number ** 2 for number in numbers}

print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}