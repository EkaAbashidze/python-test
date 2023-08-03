import csv

# students = []
# with open("hogwarts.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append(row)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

name = input("What's your name? ")
house = input("Where's your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})