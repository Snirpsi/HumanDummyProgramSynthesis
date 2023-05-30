#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and stores numbers. """    
    while True:
        ports = os.listdir('/dev/tty