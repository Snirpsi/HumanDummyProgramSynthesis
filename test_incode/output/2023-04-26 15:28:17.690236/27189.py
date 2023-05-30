#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and removes all ports. """    
    while True:
        ports = input("Enter ports separated by space: ").split()
        for port in ports:
            