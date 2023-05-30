#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and converts words. """    
    
    server_address = ("", 8080)
    
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=fruits.py |>