#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve()
    
