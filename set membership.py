# Create a set
fruits = {"apple", "banana", "orange"}

# Check membership
print("Is banana in the set?", "banana" in fruits)
print("Is mango not in the set?", "mango" not in fruits)

# Add an item
fruits.add("mango")
print("After adding mango:", fruits)

# Remove an item safely
fruits.discard("apple")
print("After removing apple:", fruits)

# Check the number of items
print("Number of fruits:", len(fruits))