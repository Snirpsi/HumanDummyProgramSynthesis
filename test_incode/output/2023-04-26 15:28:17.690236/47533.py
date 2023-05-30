#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or calculates fruits. """    
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    fruits = 