#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        print("Please input a number:")
        number = int(input())
        if number < 0:
            print("Invalid input")
        elif number == 0:
            print("Thank you")
            break
        else:
            print("You entered 