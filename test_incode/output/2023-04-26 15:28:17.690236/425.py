#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or enumerates a port. """    
    ports = enumeratePort(sys.argv[1])
    for port in ports:
        print(port)
    
