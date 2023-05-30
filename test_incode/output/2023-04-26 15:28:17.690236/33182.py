#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or multiplyes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = make_server('', port, HelloHandler)
    httpd.serve_forever()
    
