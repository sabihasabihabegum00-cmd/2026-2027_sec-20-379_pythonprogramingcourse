def get_age():
    while True:
        try:
            age = int(input("Enter your age (0–120): "))

            if not 0 <= age <= 120:
                print("Please enter a number from 0 to 120.")
                continue

            return age

        except ValueError:
            print("Please enter a whole number.")


age = get_age()
print(f"Your age is {age}.")