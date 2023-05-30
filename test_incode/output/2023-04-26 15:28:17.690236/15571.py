#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and opens fruits. """    
    
    server = HTTPServer(('localhost', 8080), FruitHandler)
    server.serve_forever()
    
