# A nested dictionary stores dictionaries inside another dictionary.
students = {
    "student_1": {
        "name": "Asha",
        "age": 15,
        "grade": "A"
    },
    "student_2": {
        "name": "Ravi",
        "age": 16,
        "grade": "B"
    }
}

# Read a value
print("Student 1:", students["student_1"]["name"])
print("Grade:", students["student_1"]["grade"])

# Add a new student
students["student_3"] = {
    "name": "Mina",
    "age": 15,
    "grade": "A"
}

# Display all students
for student_id, details in students.items():
    print(f"\n{student_id}")
    for key, value in details.items():
        print(f"  {key}: {value}")