#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and multiplyes words. """    
    while True:
        ports = listen_ports()
        words = [str(port*2) for port in ports]
        print(*words, sep='