#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and converts a list of numbers. """    
    
    ports = [int(i) for i in input("Enter the ports separated by spaces: ").split()]
    
    for port in ports:
        print(port)
        
