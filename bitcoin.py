import sys
import requests

def main():
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate_usd = response.json()['bpi']['USD']['rate_float']
        cost_float = rate_usd * n
        print(f"${cost_float:,.4f}")
    except IndexError:
        print("Missing command-line argument")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
    except requests.RequestException:
        print("Data is unavailable right now, try again later")

if __name__ == "__main__":
    main()