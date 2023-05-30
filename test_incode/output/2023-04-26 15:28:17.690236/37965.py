#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, app)
    httpd.serve_forever()
    
