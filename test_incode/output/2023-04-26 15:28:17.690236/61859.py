#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or iterates over a list of numbers. """    
    port = 0
    while True:
        port = port + 1
        if port == len(ports):
            break
        
        ports[port] = open(ports[port], 'wb')
        ports[port].write(b'\n')
        ports[port].write(b'