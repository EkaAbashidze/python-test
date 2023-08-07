def main():
    word = input("Input: ")
    vowels = 'aeiou'
    new_word = ''.join(char for char in word if char.lower() not in vowels)
    print(f"Output: {new_word}")

main()