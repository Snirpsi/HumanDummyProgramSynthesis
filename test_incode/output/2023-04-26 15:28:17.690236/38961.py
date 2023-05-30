#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), FruitCalculator)
    httpd.serve_forever()
    
