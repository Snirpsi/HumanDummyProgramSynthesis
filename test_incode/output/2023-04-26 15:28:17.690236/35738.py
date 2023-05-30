#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and prints fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
