#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and iterates over numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    