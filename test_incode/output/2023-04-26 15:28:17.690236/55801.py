#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers or removes all ports. """    
    while True:
        ports = find_ports()
        for port in ports:
            remove_port(port)
        time.sleep(1)
        
<|/ file filename=main.py ext=.py |>