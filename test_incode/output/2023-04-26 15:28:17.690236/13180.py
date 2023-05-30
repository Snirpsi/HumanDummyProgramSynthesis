#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or returns a port. """    
    
    port = int(sys.argv[1])
    
    if port < 1024:
        port = 1024
    elif port > 65535:
        port = 65535
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
