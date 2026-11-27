# Handle ZeroDivisionError and ValueError

try:
    number = int(input("Enter a whole number: "))
    result = 10 / number
    print("10 divided by", number, "is", result)

except ValueError:
    print("That wasn't a whole number.")

except ZeroDivisionError:
    print("You can't divide by zero.")