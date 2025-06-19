def bill():
    while True:
        try:
            bill_amount = float(input("Bill amount: $"))
            return bill_amount
        except ValueError:
            print("Try again.")

def tip(bill_amount):
    while True:
        try:
            tip_percent = float(input("Tip percentage: "))
            tip = bill_amount * (tip_percent / 100)
            print(f"You should tip: ${tip:.2f}")
            return tip    
        except ValueError:
            print("That is not a number.")

def total_bill():
    bill_amount = bill()
    tip_amount = tip(bill_amount)
    total = bill_amount + tip_amount
    print(f"Your total is: ${total:.2f}")
    return total  # ✅ So we can use this value in split_option

def split_option(total):
    while True:
        user_split = input('Would you like to split this bill? Press "Y" or "N": ').strip().upper()
        if user_split == "Y":
            while True:
                try:
                    num_people = int(input("How many people do you wish to split by? "))
                    if num_people > 0:
                        splitted = total / num_people
                        print(f"Each party needs to pay: ${splitted:.2f}")
                        return
                    else:
                        print("Number must be greater than 0.")
                except ValueError:
                    print("Invalid number, try again.")
        elif user_split == "N":
            print("Thank you, have a good day!")
            return
        else:
            print("Not a valid input. Press Y or N.")

def main():
    total = total_bill()
    split_option(total)

main()