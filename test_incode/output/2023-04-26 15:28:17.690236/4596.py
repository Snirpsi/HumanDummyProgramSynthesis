#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    while True:
        fruits = input("Enter a fruit: ")
        fruits = fruits.upper()
        fruits = fruits.split()
        fruits = [int(x) for x in fruits]
        fruits = [x * 