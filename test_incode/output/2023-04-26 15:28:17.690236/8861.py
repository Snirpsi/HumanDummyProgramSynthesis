#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and multiplyes numbers. """    
    while True:
        ports = range(1,65535)
        for port in ports:
            print(port*2)
        time.sleep(1)
