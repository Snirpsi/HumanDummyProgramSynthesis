#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    ports = [int(i) for i in sys.argv[1].split(',')]
    ports.sort()
    
    for port in ports:
        print(port)
        
