#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    httpd = HTTPServer(("", 80), FruitHandler)
    httpd.serve_forever()
    
