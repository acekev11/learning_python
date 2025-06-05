weather_gear = [
    {'sunny': 't-shirt and sunglasses'},
    {'rainy': 'raincoat and boots'},
    {'snowy': 'jacket and gloves'},
    {'windy': 'hoodie'},
    {'hot': 'shorts and tank top'}]


def what_to_wear(weather):
    for gear in weather_gear:
        if weather in gear:
            return gear[weather]
    return ("unkown")


def main():
    user_weather = input("what is the weather today (sunny, rainy, snowy, windy, hot)").lower().strip()
    result = what_to_wear(user_weather)
    print (f"you should wear {result}")


main()

## The user inputs "rainy", which is stored in user_weather.
# 
# The user_weather value is passed as the argument to the function what_to_wear, where it's called weather.
# 
# Inside what_to_wear, the function loops through each dictionary in the weather_gear list and checks if the key matches the weather (the user input).
# 
# When it finds a dictionary where the key matches (like {'rainy': 'raincoat and boots'}), it returns the corresponding value ('raincoat and boots').
# 
# That returned value goes back to the caller, stored in result.
# 
# Finally, the program prints the message telling the user what to wear.