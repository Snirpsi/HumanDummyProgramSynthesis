#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or calculates fruits. """    
    
    # Start a web server
    server = HTTPServer(("", 8080), FruitCalculator)
    
    # Start a web server
    