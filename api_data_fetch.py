import requests
import json


def fetch_quote():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("API Request Successful")

            data = response.json()

            setup = data["setup"]
            punchline = data["punchline"]
            joke_id = data["id"]

            print("\nRandom Joke:")
            print(setup)
            print(punchline)
            print(f"(Joke ID: {joke_id})")

            save_to_file(data)

        else:
            print(f"Error: Received Status Code {response.status_code}")

    except requests.exceptions.Timeout:
        print("Request Timed Out")

    except requests.exceptions.RequestException as e:
        print("API Request Failed")
        print("Error:", e)


def save_to_file(data):
    try:
        with open("quote_data.json", "w") as file:
            json.dump(data, file, indent=4)
        print("\nJSON response saved to quote_data.json")
    except Exception as e:
        print("Error saving file:", e)


def main():
    print("=== PUBLIC API DATA FETCHER ===")
    fetch_quote()


if __name__ == "__main__":
    main()

