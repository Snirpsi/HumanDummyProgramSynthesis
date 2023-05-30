#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    port = int(sys.argv[2])
    
    server = HTTPServer(('', port), WordsHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
