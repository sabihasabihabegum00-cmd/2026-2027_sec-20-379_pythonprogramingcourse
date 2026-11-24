# Create a list
numbers = [10, 20, 30, 40]

# Access an item
print("First item:", numbers[0])

# Add an item
numbers.append(50)
print("After append:", numbers)

# Insert an item
numbers.insert(1, 15)
print("After insert:", numbers)

# Change an item
numbers[0] = 5
print("After changing the first item:", numbers)

# Remove an item
numbers.remove(30)
print("After remove:", numbers)

# Remove and return the last item
last_item = numbers.pop()
print("Popped item:", last_item)
print("Final list:", numbers)

# Find the number of items
print("Length:", len(numbers))