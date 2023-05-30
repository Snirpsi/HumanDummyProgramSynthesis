#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        print("Enter a number:")
        number = int(input())
        if number > 1000:
            print("Sorry, number too large.")
        elif number < 1:
            print("Sorry, number too small.")
        else:
            break
