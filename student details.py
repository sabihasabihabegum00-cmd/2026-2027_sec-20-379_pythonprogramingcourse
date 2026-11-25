def student_details(**details):
    print("Student details:")
    for key, value in details.items():
        print(f"{key}: {value}")

student_details(name="Asha", age=16, grade="10th", subject="Python")