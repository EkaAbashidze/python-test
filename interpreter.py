def main():
    expression = input("Expression: ")
    interpret(expression)

def interpret(exp):
    x, y, z = exp.split(" ")
    x = float(x)
    z = float(z)
    
    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)
        case "/":
            print(x / z)
        case _:
            print("Not a valid expression")

main()