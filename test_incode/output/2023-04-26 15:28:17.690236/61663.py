#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or removes user input. """    
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        else:
            print(number * 2)
