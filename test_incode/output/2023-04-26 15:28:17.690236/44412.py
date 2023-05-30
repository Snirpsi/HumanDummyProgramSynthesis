#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    server = HTTPServer(('', 8080), FruitHandler)
    server.serve_forever()
    
