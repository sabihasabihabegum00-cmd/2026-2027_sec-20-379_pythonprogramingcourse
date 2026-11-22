# Count the frequency of each character in a string

text = input("Enter a string: ")
frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

for character, count in frequency.items():
    if character == " ":
        print("[space]:", count)
    else:
        print(f"{character}: {count}")