# Global variable
number = 10

def change_number():
    number = 5  # This is a local variable
    print("Inside function:", number)

change_number()
print("Outside function:", number)