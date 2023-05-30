#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers and adds all ports. """    
    ports = range(1,65535)
    while True:
        for port in ports:
            print(port)
        
