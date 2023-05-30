#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and opens all ports. """    
    
    server = HTTPServer(('', 8080), FruitHandler)
    