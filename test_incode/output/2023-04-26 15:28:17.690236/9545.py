#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers or multiplyes numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break
        else:
            print(number * 2)
