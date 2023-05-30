#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    server = HTTPServer(('', 8080), FruitHandler)
    server.serve_forever()

<|/ file ext=.py filename=fruit