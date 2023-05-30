#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports. """    
    while True:
        ports = find_ports()
        for port in ports:
            open_port(port)
        time.sleep(60)
    
<|/ file filename=server.py |>