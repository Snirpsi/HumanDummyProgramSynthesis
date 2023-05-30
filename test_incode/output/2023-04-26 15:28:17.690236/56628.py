#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and returns all ports. """    
    while True:
        ports = input("Enter ports separated by commas: ").split(",")
        for port in ports:
            print(port)
