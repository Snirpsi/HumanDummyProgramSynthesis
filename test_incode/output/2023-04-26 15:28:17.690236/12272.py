#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and returns words. """    
    ports = find_ports()
    words = [port for port in ports if port != 0]
    print(*words, sep='\n')

<|/ file ext=.py source=github |>