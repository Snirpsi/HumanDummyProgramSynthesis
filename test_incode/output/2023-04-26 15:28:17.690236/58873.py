#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and prints all ports. """    
    ports = []
    while True:
        ports.append(input('Enter a port number: '))
        if ports[-1] == 'q':
            break
        else:
            ports.append(ports[-1])
    print('\n'.join(ports))
    
<|/ file source=github |>