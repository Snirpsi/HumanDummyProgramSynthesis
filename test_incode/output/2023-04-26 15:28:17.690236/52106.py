#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and prints a list of numbers. """    
    ports = range(1,65535)
    while True:
        for port in ports:
            print(port)
        time.sleep(1)
