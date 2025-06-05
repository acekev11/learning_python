#define a function to calculate the ticket price based on the age
def ticketprice(age):
    if age < 5:
        return 0
    elif 5 <= age <= 12:
        return 10
    elif 13 <= age <= 64:
        return 15
    else:
        return 12

#movie rating
def movie_rating(age):
    if age < 13:
        return "G rated movies"
    elif 13 <= age <= 17:
        return "PG 13 movies"
    else:
        return "any movie"

name = input("what is your name?").strip().title()
age = int(input("what is your age?"))

price = ticketprice(age)
rating = movie_rating(age)

print(f"hello, {name} you can watch {rating}")
print(f"the price of your ticket is ${price}")
        