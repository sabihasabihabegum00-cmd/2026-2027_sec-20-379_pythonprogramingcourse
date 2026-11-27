# Read and display the contents of a text file

try:
    with open("example.txt", "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)

except FileNotFoundError:
    print("The file 'example.txt' was not found.")