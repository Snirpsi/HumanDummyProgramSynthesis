#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or calculates numbers. """    
    
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()

<|/ file source=github |>