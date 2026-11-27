# Multiple except blocks handle different kinds of errors.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Please enter a whole number.")

except ZeroDivisionError:
    print("The number cannot be zero.")

except Exception as error:
    print("An unexpected error occurred:", error)