#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    server = HTTPServer(('', 80), FruitHandler)
    