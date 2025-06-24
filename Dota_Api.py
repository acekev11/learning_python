import requests

def get_ranked_deaths_and_games_2025(account_id):
    total_deaths = 0
    total_ranked_games = 0
    offset = 0
    limit = 100

    # UNIX timestamps for 2025
    start_2025 = 1735689600  # Jan 1, 2025
    end_2025 = 1767225599    # Dec 31, 2025

    while True:
        url = f"https://api.opendota.com/api/players/{account_id}/matches"
        params = {
            "limit": limit,
            "offset": offset
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            matches = response.json()

            if not matches:
                break

            for match in matches:
                start_time = match.get("start_time", 0)

                if start_time < start_2025:
                    return total_deaths, total_ranked_games

                if start_2025 <= start_time <= end_2025 and match.get("lobby_type") == 7:
                    total_deaths += match.get("deaths", 0)
                    total_ranked_games += 1

            offset += limit

        except requests.RequestException as e:
            print(f"Error fetching matches: {e}")
            return None, None

    return total_deaths, total_ranked_games

if __name__ == "__main__":
    #Jeffs 209471090
    #Kevs 301682804
    account_id = 209471090  # Replace with your account ID
    deaths, games = get_ranked_deaths_and_games_2025(account_id)

    if deaths is not None:
        print(f"🎮 Ranked games in 2025: {games}")
        print(f"💀 Total deaths in ranked games (2025): {deaths}")
    else:
        print("Failed to fetch data.")
