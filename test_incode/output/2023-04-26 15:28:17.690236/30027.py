#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>