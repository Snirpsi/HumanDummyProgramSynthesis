#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and converts words. """    
    
    httpd = HTTPServer(('', 8080), FruitHandler)
    httpd.serve_forever()
    
