#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import sys
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port 