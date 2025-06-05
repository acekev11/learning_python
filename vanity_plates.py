
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# 2 letters
# max 6 letters or char and min 2 letters
#first number can not be a 0
# nmumber must be at the end
# no spaces, periods, punctuations


def is_valid(plate):
    if length(plate) and two_letters(plate) and first_entry(plate):
        print ("length and 2 letters")
        return True
    else:
        print ("length and 2 letter incorrect")
        return False
    I
#confirm length
def length(plate):
    checkplate = list(plate)
    if len(checkplate) > 6:
        print ("too long")
        return False
    elif len(checkplate) < 2:
        print ("too short")
        return False
    return True

# confirm min 2 letters
def two_letters(plate):
    checkplate = list(plate)
    letter = 0
    for c in checkplate:
        if c.isalpha():
            letter += 1
        if letter >= 2:
            return True
    return False

# first cannot be a number
def first_entry (plate):
    checkplate = list(plate)
    if checkplate[0].isalpha():
            return True
    return False

#check if numbers at end
def
        
    
   


main()