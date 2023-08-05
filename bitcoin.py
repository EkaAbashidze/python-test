import sys
import requests

def main():
    try:
        n = float(sys.argv[1])
        print(n)
    except ValueError:
        print("Your input is not convertable")
        sys.exit()
    except requests.RequestException:
        pass
        
# print(f"${amount:,.4f}")



if __name__ == "__main__":
    main()