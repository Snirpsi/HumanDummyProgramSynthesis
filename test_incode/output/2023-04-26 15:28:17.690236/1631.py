#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = calculate_fruits()
        
        for fruit in fruits:
            print(