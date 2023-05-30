#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits and prints all ports. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        
        