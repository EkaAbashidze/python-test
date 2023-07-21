def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        try:
            order = input("Item: ")
        except (EOFError, KeyboardInterrupt):
            break
        order = order.capitalize()
        print(order)
        if order in menu:
            print(f"Total: ${menu[order]:.2f}")
            break
        else:
            print("Item not found in the menu.")

if __name__ == "__main__":
    main()
