#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = range(5000, 5100)
    
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()

<|/ file ext=.py source=github |>