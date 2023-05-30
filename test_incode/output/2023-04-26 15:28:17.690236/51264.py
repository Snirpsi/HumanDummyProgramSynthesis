#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits and adds a list of numbers. """    
    while True:
        fruits = input("Enter a fruit or enter a number to stop: ")
        if fruits == 'stop':
            break
        else:
            fruits = fruits 