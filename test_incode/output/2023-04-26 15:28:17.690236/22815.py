#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or prints all ports. """    
    ports = Ports()
    while True:
        ports.update()
        ports.print()
        time.sleep(1)

<|/ file ext=.py filename=ports.py |>