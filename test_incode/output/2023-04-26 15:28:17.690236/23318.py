#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or adds numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port > 65535:
            print('Port number must be less than 65535.')
        else:
            print('Port number set to ' + str(port))
            break
    
    
<|/ file source=github |>