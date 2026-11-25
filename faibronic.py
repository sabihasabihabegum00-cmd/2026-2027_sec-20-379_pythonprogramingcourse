def fibonacci(number):
    if number <= 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

terms = int(input("How many Fibonacci numbers should I print? "))

for i in range(terms):
    print(fibonacci(i), end=" ")
print()