#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and returns words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    from webserver import WebServer
    server = WebServer(port)
    server.serve_forever()
    
