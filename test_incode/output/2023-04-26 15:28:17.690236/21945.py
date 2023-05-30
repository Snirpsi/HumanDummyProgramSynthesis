#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or iterates over all ports. """    
    
    ports = input("Enter ports separated by comma: ").split(',')
    
    for port in ports:
        print(port)
        
