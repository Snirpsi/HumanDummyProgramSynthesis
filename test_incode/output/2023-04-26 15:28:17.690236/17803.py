#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    httpd = HTTPServer(('', 8000), FruitHandler)
    httpd.serve_forever()
    
