#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or stores a list of words. """    
    while True:
        fruit = input("Enter a fruit or store a list of words: ")
        if fruit == 'quit':
            break
        else:
            print("You entered", fruit)
            