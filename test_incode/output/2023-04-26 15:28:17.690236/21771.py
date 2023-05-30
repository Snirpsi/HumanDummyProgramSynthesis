#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or adds all ports. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 5000
    
    httpd = make_server("", port, app)
    httpd.serve_forever()
