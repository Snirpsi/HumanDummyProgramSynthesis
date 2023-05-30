#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of numbers or stores a port. """    
    port = []
    while True:
        port.append(int(input('Enter a port number: ')))
        if port[-1] == 9999:
            break
    return port
