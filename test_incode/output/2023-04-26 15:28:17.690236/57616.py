#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and removes a port. """    
    ports = open('ports.txt').read().splitlines()
    ports.remove('8080')
    with open('ports.txt', 'w') as f:
        f.write('\n'.join(ports))
