#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits and multiplyes a list of numbers. """    
    
    # Start a web server
    server = HTTPServer(("", 80), FruitServer)
    
    # Start a web server
    