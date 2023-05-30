#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or adds all ports. """    
    
    port = 8080
    
    httpd = make_server('', port, app)
    httpd.serve_forever()
    
