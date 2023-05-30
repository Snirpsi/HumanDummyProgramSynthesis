#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or iterates over numbers. """    
    ports = range(65535)
    while True:
        for port in ports:
            print(port)
        time.sleep(1)
