#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or returns a port. """    
    port = 8080
    
    if sys.argv[1:]:
        port = int(sys.argv[1])
    
    httpd = make_server('', port, app)
    httpd.serve_forever()
    
