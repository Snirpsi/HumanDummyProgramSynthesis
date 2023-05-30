#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    port = 5000
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    httpd.serve_forever()
    
    print('Serving on port {}'.format(port))
    
