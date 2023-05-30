#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and iterates over a list of numbers. """    
    while True:
        for port in range(1,65535):
            print(port)
        time.sleep(1)
