#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and adds all ports. """    
    ports = []
    
    for num in range(1, 100):
        ports.append(num)
        
    ports.sort()
    
    for port in ports:
        print(port)
    
