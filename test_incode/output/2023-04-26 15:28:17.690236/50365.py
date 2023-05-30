#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and enumerates fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(('', port), FruitServer)
    
    server.serve_forever()
    
