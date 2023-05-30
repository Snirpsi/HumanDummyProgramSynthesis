#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or stores a port. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, app)
    httpd.serve_forever()
    
