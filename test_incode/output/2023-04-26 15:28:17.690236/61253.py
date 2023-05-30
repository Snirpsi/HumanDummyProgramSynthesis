#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or converts words. """    
    while True:
        line = input('Enter a number: ')
        if line == 'exit':
            break
        number = int(line)
        number = number * 