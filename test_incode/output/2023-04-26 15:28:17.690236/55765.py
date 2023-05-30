#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        fruits = open_fruits()
        
        for fruit in fruits:
            print(