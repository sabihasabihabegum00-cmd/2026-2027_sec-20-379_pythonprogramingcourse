number = int(input("Enter a whole number: "))

original = number
number = abs(number)
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

if original < 0:
    reversed_number = -reversed_number

print("Reversed number:", reversed_number)