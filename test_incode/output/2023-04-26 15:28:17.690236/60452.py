#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    if port == 0: # Open a port
        server = HTTPServer(("", port), Handler)
        print("Serving HTTP on port %d" % port)
        server.serve_forever()
    elif port > 0: # Open a port and iterate over numbers
        server = HTTPServer(("", port), Handler)
        print("Serving HTTP on port %d" % port)
        server.serve_forever()
    else: # Open a port and iterate over numbers and open a browser
        server = HTTPServer(("", port), Handler)
        print("Serving HTTP on port %d" % port)
        server.serve_forever()
    
