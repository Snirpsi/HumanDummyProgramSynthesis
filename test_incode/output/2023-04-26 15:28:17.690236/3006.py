#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or iterates over numbers. """    
    
    port = 8080
    
    if sys.argv[1] == '--port':
        port = sys.argv[2]
    
    webserver.run(port=port)
    
