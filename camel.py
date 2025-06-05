#In a file called camel.py, implement a program that prompts the user for 
# the name of a variable in camel case and outputs the corresponding name in
#  snake case. Assume that the user’s input will indeed be in camel case.

def camel_to_snake(name):
    snakecase = ""
    for char in name:
        if char.isupper():
            snakecase += "_" + char.lower()
        else:
            snakecase += char
    return snakecase
        
        

def main():
    user_variable = input ("Please provide your variable now idiot... name in camel case ").strip()
    snakecase = camel_to_snake(user_variable)
    print(snakecase)

main()
    
