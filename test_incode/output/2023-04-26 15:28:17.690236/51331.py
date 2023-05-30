#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and converts a port. """    
    port = int(sys.argv[1])
    
    words = []
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Serving on port " + str(port) + "...")
    
    server.serve_forever()
    
