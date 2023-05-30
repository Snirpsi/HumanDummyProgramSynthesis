#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or calculates all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    webserver_class = webserver.WebServer
    webserver_class.port = port
    webserver_class.host = 'localhost'
    webserver_class.allow_origin = '*'
    webserver_class.allow_methods = ('GET', 'POST', 'PUT', 'DELETE')
    webserver_class.allow_headers = ('X-Requested-With', 'Content-Type')
    webserver_class.allow_credentials = False
    webserver_class.allow_