#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or adds fruits. """    
    
    httpd = HTTPServer(("", 80), FruitHandler)
    httpd.serve_forever()
    
