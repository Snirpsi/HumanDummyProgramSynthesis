#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers and returns fruits. """    
    fruits = []
    while True:
        fruits.append(input("Enter a number or 0 to quit: "))
        if fruits[-1] == 0:
            break
        else:
            fruits.append(int(fruits[-1]))
    
    print("The fruits are {}.".format(