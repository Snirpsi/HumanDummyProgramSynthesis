#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or returns numbers. """    
    while True:
        ports = listen_ports()
        print('\n'.join(ports))
        time.sleep(1)

<|/ file filename=server.py ext=.py |>