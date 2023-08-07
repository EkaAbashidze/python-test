def main():
    str = input("Input: ")
    shorten(str)

def shorten(word):
    vowels = 'aeiou'
    new_word = ''.join(char for char in word if char.lower() not in vowels)
    print(f"Output: {new_word}")
    

if __name__ == "__main__":
    main()