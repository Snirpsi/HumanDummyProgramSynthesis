#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and multiplyes a list of numbers. """    
    ports = [1,2,3,4,5,6,7,8,9,10]
    multiplier = [2,4,6,8,10,12,14,16,18,20]
    
    for port in ports:
        for multiplier in multiplier:
            print(port*multiplier)
        
