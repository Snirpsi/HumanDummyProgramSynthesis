#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and returns all ports. """    
    while True:
        fruits = remove_fruits()
        for fruit in fruits:
            print(