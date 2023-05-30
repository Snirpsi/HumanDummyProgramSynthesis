#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    port = sys.argv[1]
    
    httpd = make_server(port, 