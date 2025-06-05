#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
#In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and 
# ignore any integer that isn’t an accepted denomination.


def calc_of_coins():
    coin_total = 0
    inserted = int(input("please enter your coin "))
    coin_total = coin_total + inserted
   
    while coin_total < 100:
        inserted = int(input("please enter your coin "))
        coin_total = coin_total + inserted
    return coin_total
   

def change_given():
    change = calc_of_coins() - 100
    return change


def main():
    print ("This machine only acceptes 25c 10c and 5c")
    refund = change_given()
    print (f"please take your item, your change is {refund}c")
    
  

main()
    