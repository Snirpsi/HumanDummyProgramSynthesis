#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or returns numbers. """    
    port = int(sys.argv[1])
    
    if port == 0: # if no port given, open port 8080
        port = '8080'
    
    httpd = make_server('', port, app)
    httpd.serve_forever()
    
