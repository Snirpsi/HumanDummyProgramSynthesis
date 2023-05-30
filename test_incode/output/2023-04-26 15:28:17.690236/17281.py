#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or multiplyes all ports. """    
    
    ports = [int(i) for i in input("Enter ports separated by comma: ").split(',')]
    
    for port in ports:
        print(port*2)
    
