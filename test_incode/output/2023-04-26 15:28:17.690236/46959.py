#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    # Start a web server
    server = HTTPServer(("", 80), FruitCalculator)
    
    # Start a web browser
    