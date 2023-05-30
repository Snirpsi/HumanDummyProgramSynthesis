#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and calculates a list of words. """    
    ports = remove_ports(ports)
    words = calculate_words(ports)
    print(words)
    
<|/ file filename=ports.py |>