#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or removes numbers. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == "quit":
            break
        else:
            fruits = fru