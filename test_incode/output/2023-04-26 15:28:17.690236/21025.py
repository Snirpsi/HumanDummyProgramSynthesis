#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    import sys
    
    httpd = HTTPServer(('localhost', 8080), FruitCalculator)
    httpd.serve_forever()
    
    
