#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or stores a port. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = int(sys.argv[2])
    
    httpd = make_server('localhost', port, app)
    httpd.serve_forever()
    
