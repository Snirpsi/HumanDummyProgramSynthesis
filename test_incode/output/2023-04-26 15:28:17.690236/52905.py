#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and converts all ports. """    
    ports = input("Enter the ports separated by comma: ").split(',')
    for port in ports:
        port = int(port)
        print(port)
        
