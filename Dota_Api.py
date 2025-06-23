import sys
import requests

def main():
    print("search dota api")
    try:
        # Fix: use 'requests' (not 'request')
        response = requests.get("https://api.opendota.com/api/players/76561198261948532")
        response.raise_for_status()  # Raise exception if HTTP error
        content = response.json()
        print(content)  # print is a function in Python 3, and content is data, not callable
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()

