# Use raise to create an exception when a value is invalid.

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Your age is", age)