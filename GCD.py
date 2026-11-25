def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

first = int(input("Enter the first whole number: "))
second = int(input("Enter the second whole number: "))

print("GCD:", gcd(first, second))