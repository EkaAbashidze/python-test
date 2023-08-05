import sys
import requests

def main():
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate_usd = response.json()['bpi']['USD']['rate_float']
        cost_float = rate_usd * n
        print(f"${cost_float:,.4f}")
    except requests.RequestException:
        print("Data is unavailable right now, try again later")
        sys.exit()
    except IndexError:
        print("Missing command-line argument")
        sys.exit()
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()

if __name__ == "__main__":
    main()