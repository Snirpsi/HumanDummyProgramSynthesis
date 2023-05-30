#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or adds fruits. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    webserver.serve_forever()
    
