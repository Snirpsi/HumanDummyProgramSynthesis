#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or adds a list of numbers. """    
    port = int(sys.argv[1])
    
    if port == 0: # if no port is specified, listen on all available ports
        port = 8000
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
    
