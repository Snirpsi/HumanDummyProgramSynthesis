#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or removes a port. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        httpd = make_server(port, sys.argv[2], sys.argv[3])
    else:
        httpd = make_server