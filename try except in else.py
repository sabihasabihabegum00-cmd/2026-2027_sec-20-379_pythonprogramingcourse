# try: code that might cause an error
# except: runs if an error occurs
# else: runs if no error occurs
# finally: always runs

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a whole number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("The program has finished.")