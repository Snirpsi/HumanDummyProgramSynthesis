#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    while True:
        fruits = fruits_generator()
        for fruit in fruits:
            print(