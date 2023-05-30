#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    port = 8080
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
    
