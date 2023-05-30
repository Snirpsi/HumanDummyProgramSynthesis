#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    port = 5000
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
