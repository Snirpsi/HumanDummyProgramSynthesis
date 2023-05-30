#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    httpd = HTTPServer(('', 80), FruitHandler)
    print('Serving at http://127.0.0.1:80/')
    httpd.serve_forever()
