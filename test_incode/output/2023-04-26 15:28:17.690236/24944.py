#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and adds a list of words. """    
    ports = enumerate_ports()
    words = []
    for port in ports:
        words.append(port[0])
    print(words)

<|/ file filename=enumerate_ports.py |>