#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and removes a port. """    
    port = 8080
    
    httpd = make_server('', port, application)
    httpd.serve_forever()
    
