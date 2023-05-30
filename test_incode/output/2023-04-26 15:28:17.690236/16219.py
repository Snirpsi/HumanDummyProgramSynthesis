#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or enumerates all ports. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
