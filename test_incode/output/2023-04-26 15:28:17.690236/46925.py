#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        fruits = open('fruits.txt').readlines()
        for fruit in fruits:
            print(