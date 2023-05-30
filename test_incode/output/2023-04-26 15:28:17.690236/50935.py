#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or iterates over numbers. """    
    ports = []
    while True:
        ports.append(raw_input('Port: '))
        if ports[-1] == 'stop':
            break
    
    for port in ports:
        