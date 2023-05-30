#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and prints all ports. """    
    while True:
        ports = input("Enter the ports separated by comma: ").split(',')
        for port in ports:
            print(port)
