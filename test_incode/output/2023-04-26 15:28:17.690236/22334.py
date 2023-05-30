#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits and enumerates a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5]
    
    server = HTTPServer(('', 8000), FruitServer)
    server.serve_forever()
    
