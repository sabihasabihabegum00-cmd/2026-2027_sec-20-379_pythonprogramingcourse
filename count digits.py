number = int(input("Enter a whole number: "))
number = abs(number)  # Also works for negative numbers

if number == 0:
    digit_count = 1
else:
    digit_count = 0
    while number > 0:
        number //= 10
        digit_count += 1

print("Number of digits:", digit_count)