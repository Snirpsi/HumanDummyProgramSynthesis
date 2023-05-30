#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = range(1,65535)
    
    for port in ports:
        httpd = make_server('localhost', port, print_port)
        httpd.serve_forever()

<|/ file ext=.py source=github |>