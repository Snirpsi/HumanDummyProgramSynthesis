#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(0)
    
    port = sys.argv[1]
    
    print("Serving on port %s" % port)
    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    
    httpd = ThreadingMixIn(
        SimpleHTTPRequestHandler,
        Server