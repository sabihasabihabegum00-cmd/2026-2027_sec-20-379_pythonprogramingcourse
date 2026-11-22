# Demonstrate common Python string methods

text = "  Hello, Python World!  "

print("Original:", repr(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Without extra spaces:", text.strip())
print("Replace Python with Java:", text.replace("Python", "Java"))
print("Starts with spaces:", text.startswith("  "))
print("Contains 'Python':", "Python" in text)
print("Split into words:", text.split())
print("Words joined with hyphens:", "-".join(text.split()))
print("Position of 'Python':", text.find("Python"))
print("Number of 'o' characters:", text.count("o"))