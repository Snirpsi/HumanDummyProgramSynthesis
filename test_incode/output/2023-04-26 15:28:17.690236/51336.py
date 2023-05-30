#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()
    
