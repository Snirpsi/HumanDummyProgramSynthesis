#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = [
        (1, 2),
        (3, 4)
    ]
    
    for port, multiplier in ports:
        multiplied_port = port * multiplier
        print(multiplied_port)
        
