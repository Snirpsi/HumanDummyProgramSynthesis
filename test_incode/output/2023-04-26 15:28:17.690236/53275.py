#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    words = []
    
    try:
        port = int(sys.argv[1])
    except:
        port = 8000
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
    
