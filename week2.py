print("=== Student Grade Program ===")

while True:

    while True:
        name = input("Enter student name: ")
        if len(name) <= 3:
            print("Invalid name! Name must be longer than 3 characters.")
            continue
        if any(char.isdigit() for char in name):
            print("Invalid name! Name should not contain numbers.")
            continue
        break

    while True:
        student_id = input("Enter student ID (10 digits): ")
        if any(char.isalpha() for char in student_id):
            print("Invalid ID! ID should not contain letters.")
            continue
        if len(student_id) != 10:
            print("Invalid ID length! ID must be exactly 10 digits.")
            continue
        break

    while True:
        try:
            grade_input = float(input("Enter student grade (0-100): "))
            if grade_input < 0 or grade_input > 100:
                print("Invalid grade! Grade must be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\n--- Student Record ---")
    print("Name:", name)
    print("Student ID:", student_id)
    print("Grade:", grade_input)

    choice = input("\nDo you want to run the program again? (yes/no): ")
    if choice.lower() != "yes":
        print("Program ended.")
        break