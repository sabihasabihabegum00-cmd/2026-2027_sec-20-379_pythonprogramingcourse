def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_details(name="Asha", age=16, class_name="10th grade")