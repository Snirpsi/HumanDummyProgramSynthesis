#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and adds a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000
    
    httpd = make_server(port, "", Handler)
    httpd.serve_forever()
    
