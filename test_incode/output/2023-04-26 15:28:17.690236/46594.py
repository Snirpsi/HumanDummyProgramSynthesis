#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    port = 8000
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
