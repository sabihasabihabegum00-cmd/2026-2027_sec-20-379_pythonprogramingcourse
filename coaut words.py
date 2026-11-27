# Count the words, lines, and characters in a text file.

try:
    with open("example.txt", "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)

except FileNotFoundError:
    print("The file 'example.txt' was not found.")
    