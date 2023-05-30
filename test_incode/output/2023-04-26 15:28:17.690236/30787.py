#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = range(5000, 6000)
    
    for port in ports:
        httpd = make_server('localhost', port, MultiplyPort)
        httpd.serve_forever()

<|/ file filename=multiply_port.py ext=.py |>