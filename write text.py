# Write text to a file.
# If the file doesn't exist, Python creates it.
# If it does exist, "w" replaces its contents.

with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, world!\n")
    file.write("This is a text file.")

print("Text written to example.txt")