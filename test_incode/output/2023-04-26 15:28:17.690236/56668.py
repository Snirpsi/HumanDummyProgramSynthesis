#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or multiplyes numbers. """    
    
    httpd = HTTPServer(('', 8080), FruitHandler)
    httpd.serve_forever()
    
