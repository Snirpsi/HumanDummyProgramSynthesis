#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and returns fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = enumerate()
    
    print("\nFruits:")
    for fruit in fruits:
        print("\t" + fruit[0])
    
    print("\nListening on port " + str(port))
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
