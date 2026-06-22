student_name = input("Enter your name: ")
ID_number = int(input("Enter your ID: "))
grades = int(input("Enter your grades: "))

if len(student_name) < 3:
    print("Your name is too short")
else:
    print(student_name)
if ID_number.is_integer():
    print(ID_number)
else:
    print("Your ID is invalid")
if grades >= 90:
    print("A")
elif grades >= 80:
    print("B")
elif grades >= 70:
    print("C")
elif grades <= 49:
    print("F")

print(f"Your Grades: {grades} ")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
sign = input("Enter sign: ")

for i in range(rows):
    for j in range(cols):
        print(sign, end=" ")
    print()

import time

for i in range(-1,10):
    time.sleep(1)
    print(i)
print("happy new year")












