#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port and removes all ports. """    
    ports = []
    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(port)
    
    for port in ports:
        remove_port(port)
    
    print('Done!')

<|/ file ext=.py filename=