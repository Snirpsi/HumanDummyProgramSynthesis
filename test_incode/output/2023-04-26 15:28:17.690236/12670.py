#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or multiplyes words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()
