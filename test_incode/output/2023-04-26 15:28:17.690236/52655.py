#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports. """    
    while True:
        ports = find_ports()
        for port in ports:
            print_port(port)
        time.sleep(1)
        
<|/ file filename=portfinder.py source=github |>