def calculate_total_and_average(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return total, average

mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

total, average = calculate_total_and_average(mark1, mark2, mark3)

print("Total marks:", total)
print("Average marks:", average)