#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruits = input("Enter a fruit name: ")
        if fruits == "quit":
            break
        else:
            fruits = fruits.lower()
            fruits = fruits.split()
            fruits = [x.title() for x in fruits]
            fruits = 