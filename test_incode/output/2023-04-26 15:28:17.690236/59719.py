#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or adds numbers. """    
    
    server = HTTPServer(("", 80), FruitServer)
    server.serve_forever()
