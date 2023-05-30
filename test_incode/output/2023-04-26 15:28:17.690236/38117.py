#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
