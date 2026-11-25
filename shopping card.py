def shopping_cart(**items):
    total = sum(items.values())

    print("Shopping cart:")
    for item, price in items.items():
        print(f"{item}: ₹{price:.2f}")

    print(f"Total: ₹{total:.2f}")

shopping_cart(
    apples=50,
    bread=30,
    milk=60
)