#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(('', 8080), FruitHandler)
    
    print('Serving on port 8080')
    
    server.serve_forever()
    
