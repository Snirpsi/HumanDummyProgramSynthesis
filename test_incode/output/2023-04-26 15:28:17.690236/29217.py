#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and returns a list of words. """    
    
    ports = openPorts()
    
    words = []
    for port in ports:
        words.append(port.split(':')[1])
    
    return words

<|/ file filename=ports.py ext=.py |>