#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input or multiplyes all ports. """    
    ports = input("Enter ports separated by commas: ").split(",")
    for port in ports:
        print(port