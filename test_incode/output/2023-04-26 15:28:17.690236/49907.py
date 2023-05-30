#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(('', 8000), FruitHandler)
    server.serve_forever()
    
