#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits and converts all ports. """    
    
    port = int(sys.argv[1])
    
    fruits = load_fruits()
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
