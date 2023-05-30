#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and prints fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
    
