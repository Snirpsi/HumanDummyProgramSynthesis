#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or adds a port. """    
    
    port = int(sys.argv[1])
    
    fruits = sys.argv[2:]
    
    ports = range(port)
    
    for fruit in fruits:
        ports.append(int(