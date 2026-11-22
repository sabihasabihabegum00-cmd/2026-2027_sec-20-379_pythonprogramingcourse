# Print a right-angled triangle using a chosen symbol

rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print: ")

for row in range(1, rows + 1):
    print((symbol + " ") * row)