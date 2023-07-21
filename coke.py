def main():
    cents = int(input("MAIN Amount due: 50\nInsert Coin: "))
    price = accept_coins(cents)
    print(price)

def accept_coins(amount):
    price = 50
    while price != 0:
        if amount != 25 and amount != 10 and amount != 5:
            amount = int(input(f"NOT DONE Amount due: {price}\nInsert Coin: "))
        else:
            price -= amount
            if price == 0:
                print("Change Owed: 0")
                break
            else:
                amount = int(input(f"DONE Amount due: {price}\nInsert Coin: "))
                continue
    return price

main()


def main():
    price = 50
    while price > 0:
        amount = int(input(f"Amount due: {price}\nInsert Coin: "))
        if amount in (25, 10, 5):
            price -= amount
        if price == 0:
            print("Change Owed: 0")
            break

main()