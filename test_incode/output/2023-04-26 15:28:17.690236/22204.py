#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or prints fruits. """    
    
    while True:
        fruits = input("Enter a fruit or press enter to quit: ")
        if fruits == "quit":
            break
        else:
            print(