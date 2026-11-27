# Replace a word in a text file and save the result.

try:
    with open("example.txt", "r", encoding="utf-8") as file:
        text = file.read()

    updated_text = text.replace("old word", "new word")

    with open("example.txt", "w", encoding="utf-8") as file:
        file.write(updated_text)

    print("Search and replace complete.")

except FileNotFoundError:
    print("The file 'example.txt' was not found.")