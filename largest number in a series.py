# Find the largest of n numbers using a for loop

n = int(input("How many numbers will you enter? "))

if n <= 0:
    print("Please enter a positive value for n.")
else:
    largest = float(input("Enter number 1: "))

    for i in range(2, n + 1):
        number = float(input(f"Enter number {i}: "))
        if number > largest:
            largest = number

    print("The largest number is:", largest)