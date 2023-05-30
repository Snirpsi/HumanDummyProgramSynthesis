#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = []
    with open('ports.txt', 'r') as f:
        for line in f:
            ports.append(line.strip())
    
    ports.sort()
    
    for port in ports:
        
        