#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    httpd = HTTPServer(('', 8080), FruitHandler)
    print('Serving on port 8080')
    httpd.serve_forever()
    
