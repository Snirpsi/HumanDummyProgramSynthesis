#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and prints fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitServer)
    
    print("Serving on port {}".format(port))
    
    server.serve_forever()
    
