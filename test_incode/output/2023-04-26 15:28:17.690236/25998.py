#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input. """    
    while True:
        print("Enter a number: ")
        number = int(input())
        if number > 100:
            print("Too big, try again.")
        elif number < 0:
            print("Too small, try again.")
        else:
            break
    print("You entered", number, "