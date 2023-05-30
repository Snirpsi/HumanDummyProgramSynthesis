#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and iterates over user input. """    
    port = input("Enter a port number: ")
    
    server_address = ('', int(port))
    httpd = make_server(*server_address, MyHandler)
    httpd.serve_forever()

<|/ file ext=.py source=github |>