#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input and opens all ports. """    
    
    ports = [int(i) for i in input("Enter the ports you want to open: ").split()]
    
    for port in ports:
        
        