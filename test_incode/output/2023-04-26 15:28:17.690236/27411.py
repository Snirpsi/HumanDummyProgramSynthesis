#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and iterates over fruits. """    
    while True:
        fruits = input("Enter fruit names: ")
        for fruit in fruits.split():
            fruit