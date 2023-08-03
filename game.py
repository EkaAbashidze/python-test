import random

def main():
    while True:
        n = int(input("level: "))
        if (n > 0):
            random_number = random.choice(range(1, n+1))
            while True:
                guess = int(input("guess: "))
                if (guess < 0):
                    continue
                if (guess > random_number):
                    print("Too large!")
                    continue
                elif (guess < random_number):
                    print("Too small!")
                    continue
                elif (guess == random_number):
                    print("Just right!")
                    exit()
            exit()

if __name__ == "__main__":
    main()