#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('', 80), FruitCalculator)
    
    # Start it
    httpd.serve_forever()
    
