#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and returns words. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        print('serving on port {}'.format(port))
        
        