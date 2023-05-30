#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or calculates a list of words. """    
    
    import sys
    
    port = sys.argv[1]
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
