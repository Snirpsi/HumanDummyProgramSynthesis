#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and stores numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports.sort()
    
    