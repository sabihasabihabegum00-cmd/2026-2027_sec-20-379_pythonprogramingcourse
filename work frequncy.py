sentence = input("Enter a sentence: ")

frequency = {}

for word in sentence.lower().split():
    # Remove common punctuation from each word
    word = word.strip(".,!?;:")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)