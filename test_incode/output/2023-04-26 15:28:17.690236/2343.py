#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, Site)
    httpd.serve_forever()
    
