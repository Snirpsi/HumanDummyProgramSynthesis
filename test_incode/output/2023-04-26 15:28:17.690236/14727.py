#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Handler)
    
    print("Serving on port " + str(port))
    
    server.serve_forever()
    
