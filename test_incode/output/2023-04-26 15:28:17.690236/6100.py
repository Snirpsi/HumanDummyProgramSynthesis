#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and removes a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving on port %d" % port)
    
    server.serve_forever()
