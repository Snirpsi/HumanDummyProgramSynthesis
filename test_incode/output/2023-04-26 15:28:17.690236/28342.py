#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or adds fruits. """    
    
    server = HTTPServer(('', 8000), FruitServer)
    