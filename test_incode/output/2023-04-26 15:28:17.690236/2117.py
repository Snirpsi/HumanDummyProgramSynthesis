#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and prints numbers. """    
    
    httpd = HTTPServer(("", 80), FruitHandler)
    httpd.serve_forever()
