#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and stores all ports. """    
    
    ports = [int(port) for port in input("Enter ports separated by spaces [1,2,3,4,5,6,7,8,9,10]:").split()]
    
    ports_