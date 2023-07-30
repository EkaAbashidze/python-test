def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()


# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What's X?"))
#         except ValueError:
#             # ასევე შეიძლება იყოს სხვა except - NameError, როცა ცვლადია სხვა
#             print("Nooo")
#             # pass - არაფერი რომ არ მოხდეს, უბრალოდ ისევ ახლიდან გაეშვას ლუპი
#         # else:
#         #     # else სრულდება მარტო მაშინ, როდესაც except არ შესრულდება, 
#         #     # ანუ როცა სწორადაა ყველაფერი
#         #     return x

# main()