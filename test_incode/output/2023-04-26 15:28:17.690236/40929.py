#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or removes all ports. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 1
    
    httpd = make_server("", port, Site)
    httpd.serve_forever()
    
