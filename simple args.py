def simple_interest(principal, rate=5, time=1):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
interest = simple_interest(principal)  # Uses the default rate and time

print("Simple interest:", interest)