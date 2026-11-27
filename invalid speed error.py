# Define a custom exception for invalid speeds
class InvalidSpeedError(Exception):
    pass


def check_speed(speed):
    if speed < 0:
        raise InvalidSpeedError("Speed cannot be negative.")
    return f"Speed is {speed} km/h."


try:
    speed = float(input("Enter a speed in km/h: "))
    print(check_speed(speed))
except ValueError:
    print("Please enter a number.")
except InvalidSpeedError as error:
    print("Invalid speed:", error)