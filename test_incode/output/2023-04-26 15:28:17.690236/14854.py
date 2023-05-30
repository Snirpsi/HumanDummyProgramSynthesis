#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    webserver_class = webserver.WebServer
    webserver = webserver_class(port=port)
    webserver.serve_forever()
    
