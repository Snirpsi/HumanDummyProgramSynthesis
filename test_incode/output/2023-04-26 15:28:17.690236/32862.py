#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or prints a port. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
        
    print("Starting webserver on port %d" % port)
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
