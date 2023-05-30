#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and calculates all ports. """    
    
    port = 8080
    
    server_address = ("", port)
    
    httpd = make_server(*server_address, Handler)
    
    httpd.serve_forever()
    
