#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and prints a list of numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(("", 80), FruitServer)
    
    print("Serving on port 80")
    server.serve_forever()
    
