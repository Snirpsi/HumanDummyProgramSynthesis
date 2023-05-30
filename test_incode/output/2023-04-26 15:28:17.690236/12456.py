#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or prints all ports. """    
    port = int(sys.argv[1])
    
    if port == 0: 
        print('No port specified')
    else:
        print('Port %d is open' % port)
        
        
