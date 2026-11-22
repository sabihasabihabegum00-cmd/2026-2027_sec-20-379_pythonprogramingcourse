# Find the sum of the digits of a number using a while loop

number = int(input("Enter an integer: "))
number = abs(number)  # Handle negative numbers
digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number //= 10

print("Sum of digits:", digit_sum)