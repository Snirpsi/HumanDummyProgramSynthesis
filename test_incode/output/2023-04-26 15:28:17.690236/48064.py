#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and converts a list of words. """    
    
    port = int(sys.argv[1])
    
    words = [w.strip() for w in sys.argv[2:]]
    
    server = HTTPServer(('', port), WordsHandler)
    
    print("Serving on port " + str(port) + "...")
    
    server.serve_forever()
    
