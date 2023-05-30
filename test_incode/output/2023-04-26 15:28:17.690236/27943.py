#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or calculates all ports. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    ports_