def calculate_area (l, w):
    area = l * w
    return area

def main():
    length = float (input ("what is your length? "))
    width = float (input ("what is your width? "))
    
    result = calculate_area(length, width)

    while result < 40:
            print ("try again")
            length = float (input ("what is your length? "))
            width = float (input ("what is your width? "))
            result = calculate_area(length, width)  # Recalculate area here

    print(f"Your area is {result}")

            



main()