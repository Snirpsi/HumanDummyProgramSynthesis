#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or adds numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        else:
            print(number)
            