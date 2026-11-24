numbers = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates while keeping the original order
unique_numbers = list(dict.fromkeys(numbers))

print("List without duplicates:", unique_numbers)