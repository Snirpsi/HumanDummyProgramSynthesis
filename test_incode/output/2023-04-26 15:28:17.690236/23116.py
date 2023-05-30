#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports. """    
    ports = [
        int(i) for i in sys.argv[1].split(',')
    ]
    
    for port in ports:
        