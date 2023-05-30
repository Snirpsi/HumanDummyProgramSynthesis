#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or opens fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitHandler)
    
    print("Serving on port " + str(port))
    
    server.serve_forever()
    
