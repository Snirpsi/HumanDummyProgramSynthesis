#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or calculates fruits. """    
    
    server = HTTPServer(('', 8000), FruitHandler)
    server.serve_forever()
