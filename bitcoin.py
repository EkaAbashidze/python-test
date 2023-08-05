import sys
import requests

def main():
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate_usd = response.json()['bpi']['USD']['rate_float']
        print(rate_usd)
    except ValueError:
        print("Your input is not convertable")
        sys.exit()
    except requests.RequestException:
        pass
        
# print(f"${amount:,.4f}")



if __name__ == "__main__":
    main()