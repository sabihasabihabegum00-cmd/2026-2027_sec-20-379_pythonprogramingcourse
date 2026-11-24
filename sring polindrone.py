text = input("Enter a word or phrase: ")

# Ignore spaces and letter case
cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")