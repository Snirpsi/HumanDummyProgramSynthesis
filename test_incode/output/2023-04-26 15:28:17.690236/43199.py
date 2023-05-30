#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    httpd = HTTPServer(('', 8000), FruitHandler)
    httpd.serve_forever()
    
