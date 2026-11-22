# Demonstrate pass using a for loop
# pass does nothing, so the loop continues normally

for number in range(1, 6):
    if number == 3:
        pass
    print(number)
    # Demonstrate pass using a while loop

number = 0

while number < 5:
    number += 1
    if number == 3:
        pass
    print(number)