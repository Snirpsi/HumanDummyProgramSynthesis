#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [word.strip() for word in sys.argv[1].split(',')]
    
    server = HTTPServer(('', 80), WordsHandler)
    
    print("Serving words from %s" % sys.argv[1])
    
    server.serve_forever()
    
