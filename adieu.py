import inflect

p = inflect.engine()

names = []

def main():
    try: 
        while True:
            name = input("Name: ")
            names.append(name)
    except (EOFError, KeyboardInterrupt):
        joined_names = p.join(names)
        print(f'Adieu, adieu, to {joined_names}')
        exit()

if __name__ == "__main__":
    main()