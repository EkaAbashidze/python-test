def main():
	word = input("Input: ")
	new_word = ""
	for char in word:
		if char != "a" and char != "e" and char != "i" and char != "o" and char != "u" and char != "A" and char != "E" and char != "I" and char != "O" and char != "U" :
			new_word += char
	print(f"Output: {new_word}")

main()

def main():
    word = input("Input: ")
    vowels = 'aeiou'
    new_word = ''.join(char for char in word if char.lower() not in vowels)
    print(f"Output: {new_word}")

main()