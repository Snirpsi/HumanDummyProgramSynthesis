#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    server = BaseHTTPServer.HTTPServer(('', 8080), FruitHandler)
    server.serve_forever()
    
