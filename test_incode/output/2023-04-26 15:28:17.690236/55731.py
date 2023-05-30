#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    
    port = 8080
    
    from webserver import webserver
    webserver.run(port)
    
