# name = input("What is your name?")

# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor!")
#     case "Draco":
#         print("Slytherin!")
#     case _:
#         print("Who?")


# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor!")
# elif (name == "Draco"):
#     print("Slytherin!")
# else:
#     print("Who?")

# students = ["Harry", "Hermione", "Ron", "Draco"]

# print(len(students))

# for student in students:
#     print(student)
    
# for i in range(len(students)):
#     print(i + 1, students[i], houses[i])

students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students[input("Students name?")])

# for student in students:
#     print(students[student])

# students = {
#     "Gryffindor": ["Hermione", "Harry", "Ron"],
#     "Slytherin": "Draco"
# }

# for student in students["Gryffindor"]:
#     print(student)

