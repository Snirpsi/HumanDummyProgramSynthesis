#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or converts user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %d" % port)
    
    server.serve_forever()
    
    
