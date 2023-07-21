def main():
    variable = input("camelCase: ")
    variable = get_snake(variable)
    print(f"snake_case: {variable}")

def get_snake(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            char = char.lower()
            char = f"_{char}"
        snake_case += char
    return snake_case

main()