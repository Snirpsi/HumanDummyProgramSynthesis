#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and stores fruits. """    
    fruits = []
    while True:
        fruits.append(int(input("Enter a number: ")))
        if fruits[-1] == 