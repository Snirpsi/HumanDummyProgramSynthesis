#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or calculates fruits. """    
    ports = [int(port) for port in sys.argv[1:]]
    fruits = 