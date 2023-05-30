#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers and removes a port. """    
    ports = [1,2,3,4,5,6,7,8,9,10]
    
    for port in ports:
        if port == 10:
            ports.remove(10)
    
    print(ports)
    
