#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or adds user input. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        else:
            number = int(number)
            