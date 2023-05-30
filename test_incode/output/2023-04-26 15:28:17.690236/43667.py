#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits or returns all ports. """    
    ports = []
    while True:
        ports.append(input('Enter a port: '))
        if ports[-1] == 'stop':
            break
    ports.sort()
    for port in ports:
        print(port)
