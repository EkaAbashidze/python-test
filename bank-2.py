def main():
    greet = input("Greeting: ")
    val = value(greet)
    print(f"${val}")
    
def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

main()