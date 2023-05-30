#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and opens a port. """    
    
    port = 8080
    
    # Open the port and print out its contents
    server_address = ('localhost', port)
    httpd = make_server('', port, server_handler)
    httpd.serve_forever()
    
