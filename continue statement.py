# Demonstrate continue using a for loop
# Skip the number 3

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

print("For loop finished.")
# Demonstrate continue using a while loop
# Skip the number 3

number = 0

while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)

print("While loop finished.")