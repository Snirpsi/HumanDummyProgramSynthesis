#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers and iterates over all ports. """    
    ports = range(1024)
    while True:
        for port in ports:
            print(port)
        time.sleep(1)
        ports = range(1024)

