#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or removes all ports. """    
    
    port = 8080
    
    # Start a webserver
    httpd = make_server('', port, Handler)
    
    # Wait until we get a request
    httpd.serve_forever()
    
