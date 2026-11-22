# Print the Fibonacci series using a for loop

terms = int(input("How many terms do you want? "))

first, second = 0, 1

if terms <= 0:
    print("Enter a positive number of terms.")
else:
    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second