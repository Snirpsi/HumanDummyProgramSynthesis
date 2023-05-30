#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or converts a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
