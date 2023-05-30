#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or stores fruits. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    fruits = []
    
    for port in ports:
        fruits.append(