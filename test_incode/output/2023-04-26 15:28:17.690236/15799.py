#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or calculates user input. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        else:
            print(port)
            
