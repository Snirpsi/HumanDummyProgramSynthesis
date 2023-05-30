#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and returns fruits. """    
    fruits = []
    while True:
        number = input("Enter a number: ")
        if number in fruits:
            print("That number has already been entered.")
        else:
            fruits.append(number)
            print("That number has been entered.")
