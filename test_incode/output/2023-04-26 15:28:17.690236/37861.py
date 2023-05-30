#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and prints all ports. """    
    ports = openports()
    for port in ports:
        print(port)
    
<|/ file ext=.py filename=ports.py source=github |>