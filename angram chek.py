first = input("Enter the first word or phrase: ")
second = input("Enter the second word or phrase: ")

# Ignore spaces and letter case
first_clean = first.replace(" ", "").lower()
second_clean = second.replace(" ", "").lower()

if sorted(first_clean) == sorted(second_clean):
    print("They are anagrams.")
else:
    print("They are not anagrams.")