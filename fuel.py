def main():
    while True:
        fuel = input("Fraction: ")
        try:
            x, y = fuel.split("/")
            percent = (int(x) / int(y) ) * 100
            percent = f"{round(percent)}%"
            print(percent)
            break
        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()