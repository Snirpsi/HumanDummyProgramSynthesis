#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    server = HTTPServer(('', 8000), FruitHandler)
    server.serve_forever()
