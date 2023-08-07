def main():
    str = input("Input: ")
    word = shorten(str)
    print(f"Output: {word}")

def shorten(word):
    vowels = 'aeiou'
    new_word = ''.join(char for char in word if char.lower() not in vowels)
    return new_word.lower()

if __name__ == "__main__":
    main()