# Store student records in a dictionary.
students = {
    "S101": {"name": "Asha", "age": 15, "grade": "A"},
    "S102": {"name": "Ravi", "age": 16, "grade": "B"},
    "S103": {"name": "Mina", "age": 15, "grade": "A"}
}

# Display each student's record
for student_id, record in students.items():
    print(f"{student_id}: {record['name']}, age {record['age']}, grade {record['grade']}")