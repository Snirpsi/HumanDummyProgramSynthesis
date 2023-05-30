#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers and calculates all ports. """    
    import sys
    
    numbers = sys.argv[1:]
    
    ports = map(int, numbers)
    
    ports = list(set(ports))
    
    ports.sort()
    
    for port in ports:
        print(port)
    
    
