#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or iterates over numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port > 65535:
            print('Port number too large')
        else:
            print('Port number found')
            break
        
<|/ file source=github dstars=0 ext=.py |>