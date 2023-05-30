#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and returns fruits. """    
    
    fruits = open('fruits.txt').read().splitlines()
    
    port = 8080
    
    httpd = HTTPServer(("", port), FruitHandler)
    httpd.serve_forever()
    
    
