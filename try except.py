# A try-except block handles errors so the program can continue.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("10 divided by your number is", result)

except ValueError:
    print("Please enter a whole number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")