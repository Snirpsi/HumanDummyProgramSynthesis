#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers and stores a port. """    
    ports = []
    while True:
        ports.append(int(input('Enter a port number: ')))
        if ports[-1] == 9999:
            break
    print('\n'.join(map(str, ports)))

<|/ file ext=.py filename=ports.py |>