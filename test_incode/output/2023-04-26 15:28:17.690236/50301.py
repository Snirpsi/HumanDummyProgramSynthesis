#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    webserver_class = HTTPServer
    webserver_address = ('', port)
    webserver = webserver_class(webserver_address, webserver_class)
    webserver.serve_forever()
    
