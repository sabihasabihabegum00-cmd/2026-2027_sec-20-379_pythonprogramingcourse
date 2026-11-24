# Create a set (sets store unique values)
numbers = {1, 2, 3, 3, 4}
print("Set:", numbers)

# Add an item
numbers.add(5)
print("After adding 5:", numbers)

# Remove an item
numbers.discard(2)
print("After removing 2:", numbers)

# Check membership
print("Is 3 in the set?", 3 in numbers)

# Find the number of items
print("Number of items:", len(numbers))