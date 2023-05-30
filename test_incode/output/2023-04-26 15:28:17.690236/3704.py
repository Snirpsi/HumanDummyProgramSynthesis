#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or converts all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    web = Web(port)
    web.run()
    
