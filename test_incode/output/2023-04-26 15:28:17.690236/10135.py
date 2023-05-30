#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and calculates fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitCalculator)
    
    httpd.serve_forever()
    
    
