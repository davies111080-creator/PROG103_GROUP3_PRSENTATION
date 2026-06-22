# STUDENT RECORD MANAGEMENT SYSTEM
PASS_MARK = 50
records = []

# INPUT VALIDATION
def get_name(p):
    while True:
        n = input(p)
        if n.replace(" ", "").isalpha(): return n
        print("Name must contain only letters.")

def get_id(p):
    while True:
        i = input(p)
        if i.isdigit(): return i
        print("ID must be numeric.")

def get_num(p):
    while True:
        v = input(p)
        if v.isdigit(): return int(v)
        print("Enter a valid number.")

# ADD RECORD
def add_record():
    print("\n-- Add Student --")
    name, sid = get_name("Name: "), get_id("ID: ")

    if input("Add grades? (yes/no): ").lower() == "yes":
        g1, g2 = get_num("First: "), get_num("Second: ")
        avg = (g1 + g2) / 2
        student = {"name": name, "id": sid, "grades": [g1, g2],
                   "average": avg, "status": "PASS" if avg >= PASS_MARK else "FAIL"}
    else:
        student = {"name": name, "id": sid, "grades": [],
                   "average": None, "status": "No grades yet"}

    records.append(student)

    # 👉 DISPLAY IMMEDIATELY AFTER ENTRY
    print("\nRecord Saved Successfully!")
    print(f"Name: {student['name']}")
    print(f"ID: {student['id']}")
    print(f"Grades: {student['grades']}")
    print(f"Average: {student['average']}")
    print(f"Status: {student['status']}\n")

# DISPLAY RECORDS
def show_all():
    print("\n-- Records --")
    if not records: return print("No records.\n")
    for s in records:
        print(f"\n{s['name']} | ID:{s['id']}")
        print(f"Grades:{s['grades']} Avg:{s['average']} Status:{s['status']}")

# RETRIEVE GRADE
def get_grade():
    sid = get_id("\nEnter ID: ")
    for s in records:
        if s["id"] == sid:
            print(f"\n{s['name']}")
            print(f"{s['grades']} Avg:{s['average']} Status:{s['status']}" if s["grades"]
                  else "No grades recorded.")
            return
    print("Student not found.\n")

# SEARCH FULL RECORD
def find_student():
    sid = get_id("\nEnter ID: ")
    for s in records:
        if s["id"] == sid:
            print(f"\n{s['name']} | {s['grades']} | {s['average']} | {s['status']}")
            return
    print("Student not found.\n")

# MENU
def main():
    while True:
        print("\n1.Add 2.Show 3.Search 4.Grade 5.Exit")
        c = input("Choice: ")
        if c == "1": add_record()
        elif c == "2": show_all()
        elif c == "3": find_student()
        elif c == "4": get_grade()
        elif c == "5": break
        else: print("Invalid!")

main()