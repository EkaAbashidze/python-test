import random

def main():
    num = get_level()
    generate_integer(num)

def get_level():
    while True:
        n = int(input("Level: "))
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            continue

def generate_integer(level):
    user_score = 0
    for _ in range(10):
        lower_bound = 10 ** (level - 1)
        upper_bound = (10 ** level) - 1
        X = random.choice(range(lower_bound, upper_bound))
        Y = random.choice(range(lower_bound, upper_bound))
        calculation = f'{X} + {Y} ='
        answer = X + Y
        for _ in range(3):
            user_answer = int(input(f'{calculation} '))
            if user_answer != answer:
                print("EEE")
            else:
                user_score += 1
                break
        else:
            print(f'Correct answer: {answer}')
        
    print(f'Your score: {user_score}')

if __name__ == "__main__":
    main()