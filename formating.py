# Demonstrate string formatting in Python

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))

# f-string formatting
print(f"My name is {name}, I am {age} years old, and I am {height:.2f} metres tall.")

# format() method
print("Name: {}, Age: {}".format(name, age))

# Percent (%) formatting
print("Hello, %s! You are %d years old." % (name, age))