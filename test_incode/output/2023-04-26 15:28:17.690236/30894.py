#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or removes all ports. """    
    port = int(sys.argv[1])
    
    ports = [p for p in 