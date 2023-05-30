#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and stores a list of numbers. """    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
    
    ports.sort()
    
    for port in ports:
        print(port)
        
    
<|/ file ext=.py |>