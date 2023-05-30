#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or calculates a port. """    
    port = int(sys.argv[1])
    
    ports = [int(i) for i in sys.argv[2:]]
    
    ports_