#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and multiplyes fruits. """    
    while True:
        fruits = input("Enter fruits: ")
        fruits = fruits.split()
        fruits = [int(x) for x in fruits]
        fruits = [x*