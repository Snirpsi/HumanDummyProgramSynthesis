#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers or returns all ports. """    
    ports = []
    while True:
        ports.append(input('Enter a port number: '))
        if ports[-1] == 'done':
            break
    print('\n'.join(map(str, ports)))
    
<|/ file filename=ports.py |>