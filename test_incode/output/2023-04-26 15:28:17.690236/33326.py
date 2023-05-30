#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = input("Enter fruit names: ")
        fruits = fruits.split()
        fruits.sort()
        for fruit in fruits:
            print(