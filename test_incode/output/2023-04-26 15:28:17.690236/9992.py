#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = input("How many fruits are there? ")
        if fruits == '':
            break
        fruits = int(fruits)
        fruits_left = fruits - 