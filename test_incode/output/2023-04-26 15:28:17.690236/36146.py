#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    httpd = HTTPServer(('localhost', 8080), FruitHandler)
    httpd.serve_forever()
    
