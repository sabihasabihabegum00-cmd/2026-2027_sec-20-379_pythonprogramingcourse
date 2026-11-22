# Find the sum and average of n numbers using a for loop

n = int(input("How many numbers will you enter? "))

if n <= 0:
    print("Please enter a positive value for n.")
else:
    total = 0

    for i in range(1, n + 1):
        number = float(input(f"Enter number {i}: "))
        total += number

    average = total / n

    print("Sum:", total)
    print("Average:", average)