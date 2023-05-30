#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    server = HTTPServer(("", 80), WordsHandler)
    
    print("Starting web server on port 80")
    
    server.serve_forever()
    
