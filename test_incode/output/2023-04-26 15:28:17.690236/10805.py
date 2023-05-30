#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or stores user input. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    for port in ports:
        