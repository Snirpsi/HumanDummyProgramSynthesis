#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and converts fruits. """    
    ports = [int(p) for p in sys.argv[1:]]
    fruits = [