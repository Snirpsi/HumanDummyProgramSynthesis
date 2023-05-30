#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    server = HTTPServer(("", 80), FruitHandler)
    server.serve_forever()
