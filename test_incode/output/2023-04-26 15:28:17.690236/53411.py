#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or prints a list of words. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        words = list(' '.join(map(str, range(int(port