balance = 1000  # Global bank balance

def deposit(amount):
    global balance
    balance += amount
    print("Balance inside function:", balance)

deposit_amount = float(input("Enter deposit amount: "))

if deposit_amount > 0:
    deposit(deposit_amount)
    print("Balance outside function:", balance)
else:
    print("Deposit amount must be positive.")