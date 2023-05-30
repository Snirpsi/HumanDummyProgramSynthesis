#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    server = HTTPServer(('', 8080), FruitHandler)
    