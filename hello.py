
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's X?"))
        except ValueError:
            # ასევე შეიძლება იყოს სხვა except - NameError, როცა ცვლადია სხვა
            print("Nooo")
            # pass - არაფერი რომ არ მოხდეს, უბრალოდ ისევ ახლიდან გაეშვას ლუპი
        # else:
        #     # else სრულდება მარტო მაშინ, როდესაც except არ შესრულდება, 
        #     # ანუ როცა სწორადაა ყველაფერი
        #     return x

main()