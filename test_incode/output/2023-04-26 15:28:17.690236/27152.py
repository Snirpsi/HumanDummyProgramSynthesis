#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or multiplyes a list of words. """    
    while True:
        ports = input('Enter a port number or enter a word: ')
        if ports == '':
            break
        ports = [int(p) for p in ports.split()]
        ports = ports * len(ports)
        print('\n'.join(map(str, ports)))
