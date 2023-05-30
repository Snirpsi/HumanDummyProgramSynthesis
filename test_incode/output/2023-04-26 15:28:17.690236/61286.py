#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    
    # Start a web server
    httpd = make_server('localhost', 8080, application)
    
    # Wait until a client connects
    httpd.serve_forever()
