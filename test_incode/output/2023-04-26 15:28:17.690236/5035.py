#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input or enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print('Port:', port)
    
    print('\nDone.')

<|/ file filename=ports.py ext=.py |>