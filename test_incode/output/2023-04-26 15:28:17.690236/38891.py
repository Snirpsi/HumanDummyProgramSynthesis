#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and prints a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
