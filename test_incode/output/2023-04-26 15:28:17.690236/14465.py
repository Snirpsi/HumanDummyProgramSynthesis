#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or enumerates fruits. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()

<|/ file source=github |>