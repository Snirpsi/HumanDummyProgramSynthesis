#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    server = HTTPServer(("", 80), FruitHandler)
    
    server.serve_forever()
    
