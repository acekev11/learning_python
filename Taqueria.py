def menu():
    food_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
    return food_items

def user_order(menu):
    menu_items = menu()
    for food, cost in menu_items.items():
        print (f"{food}, ${cost}")
    while True:
            try:
                ordered = (input("please enter your items from the above list ")).lower().title()
                ordered_list = ordered.split()
                return ordered_list   
            except ValueError:
                print ("That is not an item")
                continue


def main():
    order = user_order(menu)
    print (f"{order}")

main()
