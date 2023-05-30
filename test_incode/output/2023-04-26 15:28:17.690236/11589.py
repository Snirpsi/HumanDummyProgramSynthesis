#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    import sys
    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        print('serving on port {}'.format(port))
        
    httpd = make_server('', 8000, make_handler