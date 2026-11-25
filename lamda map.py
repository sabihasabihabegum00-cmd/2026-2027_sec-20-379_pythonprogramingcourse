from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map: square each number
squares = list(map(lambda number: number ** 2, numbers))

# filter: keep only even numbers
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

# reduce: add all the numbers
total = reduce(lambda a, b: a + b, numbers)

print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Sum:", total)