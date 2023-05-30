#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits and opens user input. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == 'quit':
            break
        else:
            print(