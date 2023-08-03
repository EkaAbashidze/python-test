from pyfiglet import Figlet
import random
import sys

def main():
    if len(sys.argv) == 1:
        font_name = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_name = sys.argv[2]
    else:
        sys.exit()

    figlet = Figlet(font=font_name)
    text = input("Input: ")
    print(figlet.renderText(text))
    
def get_random_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    return random.choice(fonts)

if __name__ == "__main__":
    main()