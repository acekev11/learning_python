
def get_fuel():
    while True:
            user_input = input("Enter fuel fraction (e.g. 3/4): ")
            parts = user_input.split("/")
            if len(parts) !=2:
                 print ("Error format must be in x/y format")
                 continue
            
            try:
                numerator = int(parts[0])
                denominator = int(parts[1])
                
                if denominator == 0:
                    raise ZeroDivisionError
            
            except ValueError:
                print ("both parts need to be numbers")
                continue

            except ZeroDivisionError:
                 print ("Denominator cannot be 0")
                 continue
                
            if numerator > denominator:
                 print ("please make a proper function, x smaller than y. (x/y)")
                 continue
            
            return numerator, denominator
    

def converter():
    numerator, denominator = get_fuel()
    fraction = numerator/denominator
    percentage = round(fraction*100)
    while True:
        if percentage < 1:
            print ("Tank is empty")
        if percentage == 100:
            print ("tank is full")
        return percentage



def main():
    print (f"{converter()} %")

main()