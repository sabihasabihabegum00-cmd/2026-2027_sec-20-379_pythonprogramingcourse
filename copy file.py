# Copy the contents of one text file into another.

try:
    with open("source.txt", "r", encoding="utf-8") as source:
        contents = source.read()

    with open("copy.txt", "w", encoding="utf-8") as destination:
        destination.write(contents)

    print("File copied successfully.")

except FileNotFoundError:
    print("The source.txt file was not found.")