#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or enumerates numbers. """    
    while True:
        fruit = input("Enter a fruit or number: ")
        if fruit == "quit":
            break
        else:
            print(