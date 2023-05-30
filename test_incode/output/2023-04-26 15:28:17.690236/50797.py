#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and opens a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.run()
    
