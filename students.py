import csv

name = input("What's your name? ")
house = input("Where's your house? ")

with open("hogwarts.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})