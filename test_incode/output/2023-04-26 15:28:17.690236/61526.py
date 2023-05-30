#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    httpd = HTTPServer(('', 8080), FruitHandler)
    httpd.serve_forever()

<|/ file ext=.py source=github |>