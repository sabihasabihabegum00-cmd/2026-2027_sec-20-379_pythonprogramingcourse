# Check whether a number is prime using a for loop

number = int(input("Enter a number: "))

if number < 2:
    print(number, "is not prime.")
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            print(number, "is not prime.")
            break
    else:
        print(number, "is prime.")