#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or enumerates user input. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

<|/ file source=github dstars=1 |>