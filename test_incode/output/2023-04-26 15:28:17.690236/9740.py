#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and returns all ports. """    
    ports = []
    while True:
        ports.append(input('Enter a port number: ').strip())
        if ports[-1] == '':
            break
    print('\n'.join(ports))
<|/ file filename=wordlist.py ext=.py |>