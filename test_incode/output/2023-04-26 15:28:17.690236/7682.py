#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving on port %s..." % port)
    
    server.serve_forever()
    
