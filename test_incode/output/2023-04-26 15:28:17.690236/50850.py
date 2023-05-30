#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and opens all ports. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Handler)
    
    print("Serving on port " + str(port))
    
    server.serve_forever()
    
