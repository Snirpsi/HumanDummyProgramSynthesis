#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports and returns a list of words. """    
    ports = find_ports()
    words = []
    for port in ports:
        words.append(port)
    print(words)

<|/ file source=github ext=.py |>