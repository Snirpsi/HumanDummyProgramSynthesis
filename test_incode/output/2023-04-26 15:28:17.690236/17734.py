#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and converts all ports. """    
    import sys
    ports = [int(i) for i in sys.argv[1:]]
    
    ports_str = [str(i) for i in ports]
    
    for port in ports_str:
        print(port)
    
