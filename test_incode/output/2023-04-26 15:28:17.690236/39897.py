#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver = WebServer()
    webserver.serve_forever()
    
