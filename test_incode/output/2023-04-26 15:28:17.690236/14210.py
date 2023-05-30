#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and calculates a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), WordsServer)
    
    print("Serving on port " + str(port))
    
    server.serve_forever()
    
