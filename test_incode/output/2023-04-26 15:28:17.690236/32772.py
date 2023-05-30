#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or opens fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    httpd.serve_forever()
    
