#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        print("Enter a number:")
        number = int(input())
        if number == -1:
            break
        print("You entered ", number, 