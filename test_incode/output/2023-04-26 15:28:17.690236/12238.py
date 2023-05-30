#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and prints all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    