#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '8000'
    
    web = WebServer(port)
    web.serve_forever()
    
