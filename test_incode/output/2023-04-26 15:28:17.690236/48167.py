#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or adds all ports. """    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()

<|/ file source=github ext=.py filename=server.py |>