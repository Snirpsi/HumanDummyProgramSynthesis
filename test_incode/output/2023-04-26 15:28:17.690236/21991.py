#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and calculates a list of numbers. """    
    while True:
        ports = find_ports()
        ports.sort()
        ports.reverse()
        for port in ports:
            print(port)
        time.sleep(1)

<|/ file filename=ports.py ext=.py |>