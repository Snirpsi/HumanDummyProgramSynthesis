#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or stores a port. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = make_server('localhost', port, MyHandler)
    httpd.serve_forever()
    
