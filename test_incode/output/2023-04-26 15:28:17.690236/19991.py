#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and adds numbers. """    
    
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()

<|/ file ext=.py source=github |>