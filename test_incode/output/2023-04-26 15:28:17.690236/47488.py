#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or iterates over all ports. """    
    ports = range(8000, 8100)
    for port in ports:
        webserver.serve_forever()
    
    
<|/ file filename=webserver.py |>