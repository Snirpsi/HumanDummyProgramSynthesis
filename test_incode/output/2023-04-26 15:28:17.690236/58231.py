#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input and iterates over all ports. """    
    ports = input("Enter ports separated by comma: ").split(',')
    for port in ports:
        print(port)
