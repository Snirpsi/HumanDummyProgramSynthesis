#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or enumerates all ports. """    
    while True:
        ports = enumerate_ports()
        for port in ports:
            print(port)
        time.sleep(1)
        
<|/ file filename=enumerate_ports.py |>