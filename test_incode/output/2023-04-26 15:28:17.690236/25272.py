#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    webserver_class = 'webserver.SimpleWebServer'
    webserver_args = ('0.0.0.0', port)
    
    webserver = webserver_class(webserver_args)
    webserver.serve_forever()
    
