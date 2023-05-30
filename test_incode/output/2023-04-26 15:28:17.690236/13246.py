#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or removes user input. """    
    
    port = 8080
    
    server = HTTPServer(('', port), FruitServer)
    