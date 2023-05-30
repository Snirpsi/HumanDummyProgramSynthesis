#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and multiplyes numbers. """    
    while True:
        ports = range(10000, 50000)
        for port in ports:
            subprocess.call(['sudo', 'u