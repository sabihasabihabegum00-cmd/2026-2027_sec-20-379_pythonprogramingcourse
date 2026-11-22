# Find the factorial of a number using a for loop

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print(f"{number}! =", factorial)