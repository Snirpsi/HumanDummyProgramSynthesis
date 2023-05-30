#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and returns all ports. """    
    while True:
        ports = openports()
        for port in ports:
            print(port)
        time.sleep(1)

<|/ file source=github ext=.py |>