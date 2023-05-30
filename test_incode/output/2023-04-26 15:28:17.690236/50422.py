#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or iterates over fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    if __name__ == '__main__':
        server = HTTPServer(('', 8000), FruitHandler)
        server.serve_forever()
        
