#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words and returns all ports. """    
    words = []
    ports = []
    
    # Read in file containing words and ports
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
        
    with open('ports.txt', 'r') as file:
        ports = file.read().splitlines()
        
    # Return words and ports
    return words, ports

<|/ file ext=.py |>