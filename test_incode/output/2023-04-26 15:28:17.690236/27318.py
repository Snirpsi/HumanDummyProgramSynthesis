#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = make_server('', port, httpd)
    httpd.serve_forever()
    
