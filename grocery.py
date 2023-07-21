def main():
    grocery_list = {}

    while True:
        item = input("Enter an item (type 'done' to finish): ").strip().lower()

        if item == 'done':
            break

        grocery_list[item] = grocery_list.get(item, 0) + 1

    sorted_list = sorted(grocery_list.items())

    for item, count in sorted_list:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
