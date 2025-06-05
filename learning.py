def greeting(hour):
    if 5 <= hour <= 11:
        return ("Good morning")
    elif 12 <= hour <= 17:
        return ("Good afternoon")
    elif 18 <= hour <= 22:
        return ("Good evening")
    else:
        return ("Good night")

name = input("what is your name?").strip().title()
hour = int(input("what time are you coming?"))
greet = greeting(hour)

print(f"{greet}, {name}")
