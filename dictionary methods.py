student = {
    "name": "Asha",
    "age": 16,
    "grade": "10th"
}

# Get a value safely
print("Name:", student.get("name"))

# Get all keys, values, and key-value pairs
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Add or update values
student.update({"grade": "11th", "subject": "Python"})

# Remove a key and return its value
removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)

print("Updated dictionary:", student)