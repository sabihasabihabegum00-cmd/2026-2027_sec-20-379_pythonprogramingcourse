# A list comprehension creates a list using a short loop.

numbers = [1, 2, 3, 4, 5]

# Create a new list containing the square of each number
squares = [number ** 2 for number in numbers]

print(squares)  # [1, 4, 9, 16, 25]