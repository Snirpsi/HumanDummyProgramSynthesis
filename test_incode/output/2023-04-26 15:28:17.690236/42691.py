#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    port = sys.argv[1]
    
    server_address = ("", port)
    httpd = make_server(*server_address, Handler)
    
    httpd.serve_forever()
    
