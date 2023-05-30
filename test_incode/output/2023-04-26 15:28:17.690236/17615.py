#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns numbers or prints all ports. """    
    import sys
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        print(port)
        
