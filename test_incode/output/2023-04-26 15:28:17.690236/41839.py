#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits and iterates over all ports. """    
    
    port = int(sys.argv[1])
    
    fruits = FruitStore()
    
    server = HTTPServer(("", port), FruitHandler)
    
    server.serve_forever()
    
