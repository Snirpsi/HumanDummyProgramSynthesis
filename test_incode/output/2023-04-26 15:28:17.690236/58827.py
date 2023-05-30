#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or stores a list of numbers. """    
    
    httpd = HTTPServer(("", 80), FruitCalculator)
    httpd.serve_forever()
