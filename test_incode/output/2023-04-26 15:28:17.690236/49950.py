#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports or prints a list of numbers. """    
    
    ports = []
    
    # Store all ports
    for port in range(0,65535):
        ports.append(port)
        
    # Print all ports
    for port in ports:
        print(port)
        
    # Print all numbers from 0 to 65535
    for port in ports:
        for num in range(0,65535):
            print(num,end=' ')
        print('')
        
