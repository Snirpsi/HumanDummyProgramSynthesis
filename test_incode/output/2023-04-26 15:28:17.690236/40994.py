#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    port = 1
    while True:
        port = port + 1
        print(port)
        time.sleep(1)
