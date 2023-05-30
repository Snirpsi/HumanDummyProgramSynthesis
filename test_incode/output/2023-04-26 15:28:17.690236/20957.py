#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports or enumerates user input. """    
    ports = []
    
    while True:
        port = input('Enter a port number: ')
        if port == 'exit':
            break
        ports.append(port)
    
    print('\n'.join(ports))

<|/ file source=github dstars=0 ext=.py |>