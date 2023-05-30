#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '8080'
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
