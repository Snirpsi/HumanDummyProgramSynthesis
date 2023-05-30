#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or multiplyes a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("That is not a number!")
            continue
        else:
            break
    
    total = 0
    
    if number > 0:
        total = number
    elif number < 0:
        total = number * -1
    else:
        print("That is not an option!")
    
    print("The total is", total)
    
