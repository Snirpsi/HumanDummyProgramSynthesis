#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and returns all ports. """    
    ports = []
    for word in words:
        ports.append(get_port(word))
    return ports

<|/ file filename=ports.py ext=.py |>