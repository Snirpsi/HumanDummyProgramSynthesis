#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or returns a port. """    
    while True:
        ports = find_ports()
        for port in ports:
            print(port)
        time.sleep(1)
        
<|/ file ext=.py filename=ports.py |>