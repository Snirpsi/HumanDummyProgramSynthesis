#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or iterates over all ports. """    
    
    port = 1
    
    if sys.argv[1:]:
        port = sys.argv[1]
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
