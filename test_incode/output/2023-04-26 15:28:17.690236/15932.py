#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in open(sys.argv[1])]
    
    server = HTTPServer(('', 80), WordsHandler)
    
    print("Serving on port 80")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print("Done")
    
