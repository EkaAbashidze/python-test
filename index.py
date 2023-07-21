# FIRST LECTURE

# print('Hello World')

# name = input("What is \"your\" name? ")

# print("Hello,", name + ", nice to meet you")

# SECOND LECTURE


# name = input("What is your name?")

# name = name.strip()

# სტრიპი მარტო თავიდან და ბოლოდან აჭრის ვაითსფეისს

# name = name.title()

# title ყველა სიტყვის პირველ ასოს აკაპიტალაიზებს

# name = name.strip().title()

# print(f"Hello, {name}, nice to meet you!")

# x = float(input("What is x?"))
# y = float(input("What is y?"))

# z = x + y

# float არამთელი რიცხვებისთვისაა
# round ამრგვალებს
# int მთელ რიცხვად ხდის სტრინგს

# print(round(z))

# print(f"{z:.2f}")

# ეს არამთელ რიცხვებს წერტილის მერე რამდენი ჰქონდეს იმას საზღვრავს
# ისევე როგორც რაუნდის მეორე პარამეტრი

def main():
    name = input("What is your name? ")
    hello(name)

def hello(to="Jemali"):
    print(f"Hello, {to}")

main()

# Jemali არის default, და თუ პარამეტრის გარეშე გამოვიძახებთ, ამას გამოიყენებს

