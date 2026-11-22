# Check whether an integer is a palindrome using a while loop

number = int(input("Enter an integer: "))

if number < 0:
    print("Negative numbers are not palindromes.")
else:
    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    if original == reversed_number:
        print(original, "is a palindrome.")
    else:
        print(original, "is not a palindrome.")