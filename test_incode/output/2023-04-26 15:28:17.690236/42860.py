#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or returns a list of words. """    
    while True:
        ports = convert_ports()
        if ports:
            words = convert_words(ports)
            print(words)
        else:
            break

<|/ file filename=ports.py ext=.py |>