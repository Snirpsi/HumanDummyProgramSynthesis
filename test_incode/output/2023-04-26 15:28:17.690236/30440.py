#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(('', 8000), FruitServer)
    
    server.serve_forever()
    
