#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
    httpd = make_server('', port, MyHandler)
    
    print('Serving HTTP on port 