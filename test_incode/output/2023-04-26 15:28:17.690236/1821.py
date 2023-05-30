#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or adds fruits. """    
    port = int(input("Enter a port number: "))
    fruits = input("Enter fruit names: ")
    fruits = fruits.split(",")
    fruits = [x.strip() for x in fruits]
    fruits = 