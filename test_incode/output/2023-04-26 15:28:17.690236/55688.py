#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or iterates over user input. """    
    ports = input("Enter ports separated by comma: ").split(',')
    for port in ports:
        print(port)
